from posts import models
from django.contrib import messages
from django.views import generic
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()



class PostListView(generic.ListView, SelectRelatedMixin):
    model = models.Post
    select_related = ['user','group']


class UserPostView(generic.ListView):
    model = models.Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(
            username__iexact=self.kwargs.get('username')
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetailView(generic.DetailView, SelectRelatedMixin):
    model = models.Post
    select_related = ('user', 'group')


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePostView(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):

    fields=('title','text','group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'POST DELETED')
        return super().delete(*args, **kwargs)

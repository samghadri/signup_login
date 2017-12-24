from . import models
from django.views import generic
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
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
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_user'] = self.post_user
        return context

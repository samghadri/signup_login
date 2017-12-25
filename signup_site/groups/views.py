from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Group, GroupMember
# from . import models



class CreateGroupView(LoginRequiredMixin,generic.CreateView):
    model = Group
    fields = ('name', 'description')

class SingleGroupView(generic.DetailView):
    model = Group

class ListGroupView(generic.ListView):
    model = Group

class JoinGroupView(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=request.user, group = group)

        except IntegrityError:
            messages.warning(self.request,('You are already member of {}'.format(group.name)))

        else:
            messages.success(self.request, 'You are now a Member of {}'.format(group.name))

        return super().get(request, *args, **kwargs)

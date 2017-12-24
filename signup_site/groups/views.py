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

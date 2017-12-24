from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.text import slugify
from django import template
register = template.Library()
from django.contrib.auth import get_user_model
User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(max_length=1000)
    members = models.ManyToManyField(User, through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')

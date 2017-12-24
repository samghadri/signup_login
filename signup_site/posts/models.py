from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
User = get_user_model
from groups.models import Group



class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=50)
    text = models.CharField()
    created_date = mdoels.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group,related_name='groups',null=True,blank=True)


    def __str__(self):
        return self.title


    def save(self, *args, **kwarg):
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.username,
                                              'pk': self.pk})

    class Meta:
        ordering = ['-created_date']
        unique_together = ['username', 'title']

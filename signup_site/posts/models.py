from django.db import models
from django.core.urlresolvers import reverse
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)
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
        unique_together = ['user', 'title']

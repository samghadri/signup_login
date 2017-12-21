from django.db import models
from django.django.contrib.auth import get_user_model
User = get_user_model


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')

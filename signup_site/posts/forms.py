from django import forms
from posts import models

class PostForm(forms.ModelForm):
    model = models.Post
    fields =('title', 'text', 'group')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (models.Group.objects.filter(pk__in=user.groups.values_list("group__pk")))

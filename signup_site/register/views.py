from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView, TemplateView

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'register/signup.html'

class TestPage(TemplateView):
    template_name = 'register/test.html'

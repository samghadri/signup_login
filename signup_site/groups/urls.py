from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'new/$',views.CreateGroupView.as_view(), name='create'),



]

from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^new/$',views.CreateGroupView.as_view(), name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroupView.as_view(), name='single'),
    url(r'^$',views.ListGroupView.as_view(), name='all'),
    url(r'join/(?P<slug>[-\w]+)/$', views.JoinGroupView.as_view(), name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$', views.LeaveGroupView.as_view(), name='leave'),

]

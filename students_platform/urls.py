from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.forum_list),
#	url(r'^$', views.post_list),
	url(r'^forum/(?P<pk>[0-9]+)/$', views.forum_details),
	url(r'^forum/post/(?P<pk>[0-9]+)/$', views.post_details),
    url(r'^forum/post/new/$', views.post_new, name='post_new'),
    url(r'^forum/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

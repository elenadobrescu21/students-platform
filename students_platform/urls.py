from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.forum_list),
    url(r'^forum/(?P<forum_name>)/$', views.post_list),
	url(r'^forum/(?P<forum_name>)/post/(?P<pk>[0-9]+)/$', views.post_detail),
]

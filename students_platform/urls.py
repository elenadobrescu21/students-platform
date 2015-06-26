from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.forum_list),
	url(r'^$', views.post_list),
]


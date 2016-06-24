from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	snt,
	post_detail,
	post_update,
	post_delete,

	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
	url(r'^snt/$', snt, name='sntcouncil'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

	# url(r'^snt/$', "posts.views.snt"),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

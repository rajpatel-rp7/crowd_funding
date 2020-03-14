# coding: utf-8

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.entries, name='entries'),
    url(r'^(?P<slug>[-\w]+)/$', views.entry, name='entry'),
]

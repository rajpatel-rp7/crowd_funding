"""Crowd_funding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from projects.views import projects_list, home

urlpatterns = [
    url(r'^$', home),
    url(r'^project_list/', projects_list),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apiapp.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^oauth', include('social_django.urls',namespace="social")),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

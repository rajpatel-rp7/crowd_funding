from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^Contectus/$', views.Contectus, name='Contectus'),
    url(r'^projects_list/$', views.projects_list, name='projects_list'),
    url(r'^my/$', views.my_projects, name='my_projects'),
    url(r'^add/$', views.create_project, name='create_project'),
    url(r'^(?P<slug>[\w-]+)/$', views.single_project, name='single_project'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_project, name='edit_project'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_project, name='delete_project'),
]

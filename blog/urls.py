from django.conf.urls import include, url, patterns
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.thoughts, name='thoughts'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^thoughts/', views.thoughts, name='thoughts'),
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^links/', views.links, name='links'),
    url(r'^cv/', views.cv, name='cv'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^responsive/', views.responsive, name='responsive'),
    url(r'^header/', views.header, name='header'),
    url(r'^content/', views.content, name='content'),
    url(r'^basic/', views.basic, name='basic'),
    url(r'^basic_with_responsive_header/', views.basic_with_responsive_header, name='basic_with_responsive_header'),
    url(r'^basic_with_django_girls_content/', views.basic_with_django_girls_content, name='basic_with_django_girls_content')

)

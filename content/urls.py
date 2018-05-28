from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.content_list, name='content_list'),
    url(r'^category/(?P<category>\d+)/$', views.content_category, name='content_category'),
    url(r'^register/$', views.content_register, name='content_register'),
    url(r'^detail/(?P<pk>\d+)/$', views.content_detail, name='content_detail'),
]
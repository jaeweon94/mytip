from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.register_form, name='register_form'),
    url(r'^complete/$', views.register_complete, name= 'register_complete'),
]
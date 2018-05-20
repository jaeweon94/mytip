from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.content_list, name='content_list'),

]
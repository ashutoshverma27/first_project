from django.conf.urls import patterns, include, url
from . import views
urlpatterns=[path('',views.hello,name='hello')]

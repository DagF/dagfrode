# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home_view'),
]

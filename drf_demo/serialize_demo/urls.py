# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 16:55
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
from django.urls import path
from . import views

urlpatterns = [
    path("serializers/", views.StudentView.as_view()),
    path("serializers01/", views.StudentView01.as_view())
]

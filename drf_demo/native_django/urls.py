# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 00:11
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('students/', views.StudentView.as_view()),
    re_path('^students/(?P<pk>\d+)/', views.StudentInfoView.as_view())
]

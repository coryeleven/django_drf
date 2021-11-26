# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/19 6:01 下午
@File ： urls.py
@IDE  ： PyCharm
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # 列表视图
    url(r'^books/$', views.BookListView.as_view()),
    # 详情视图
    url(r'^books/(?P<pk>\d+)$', views.BoolDetailView.as_view())

]

# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/19 6:01 下午
@File ： urls.py
@IDE  ： PyCharm
"""

from django.conf.urls import url
from . import ModelViewSet_views as views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #     # 列表视图
    #     url(r'^books/$', views.BookListView.as_view()),
    #     # 详情视图
    #     url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

]
router = DefaultRouter()  # 创建路由器
router.register(r'books', views.BookInfoView)  # 注册路由
urlpatterns += router.urls

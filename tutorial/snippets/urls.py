# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 9:10 下午
@File ： urls.py
@IDE  ： PyCharm
"""
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import serializers

urlpatterns = [
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    # 基于类的视图
    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    # 基于api_view装饰器的视图
    # url(r'^snippets/$', views.snippet_list_api),
    # url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail_api),

    # 基于APIView装饰器视图
    url(r'^snippets/$', views.SnippetList_APIView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail_APIView.as_view()),

    # 身份验证与权限
    url(r'^users/$', views.UserList_Auth.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail_Auth.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

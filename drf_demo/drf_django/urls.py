# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 15:29
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com

from rest_framework.routers import DefaultRouter
from .views import StudentModelView

route = DefaultRouter()  # 处理试图的路由器
route.register('students2', StudentModelView, basename='students2')  # 向路由器注册试图集
# 路由列表
urlpatterns = [] + route.urls  # 将路由器中的所有列表追加到django 的路由器列表中

# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/19 3:06 下午
@File ： serializers.py
@IDE  ： PyCharm
"""
from django.contrib.auth.models import User, Group
from rest_framework import serializers


# 超链接关系，使用 HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 10:41 下午
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
from rest_framework import serializers
from .models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    """定义序列化器"""

    class Meta:
        model = BookInfo  # 指定序列化从哪个模型映射字段
        fields = "__all__"  # 映射哪些字段

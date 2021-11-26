# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/26 5:34 下午
@File ： serializers.py
@IDE  ： PyCharm
"""

from models import EnvList
from rest_framework import serializers


class EnvListModelSerializer(serializers.ModelSerializer):
    """定义模型序列化器"""

    class Meta:
        model = EnvList  # 指定序列化器字段从哪个模型去映射
        filed = '__all__'  # 映射Models类中哪些字段

# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 15:24
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com
from rest_framework import serializers
from native_django.models import Student


# 创建序列化类，在试图中调用
class StudentModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ["id","name"]
        fields = "__all__"

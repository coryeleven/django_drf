import json

from django.shortcuts import render
from rest_framework import serializers
from django.views import View
from .serializers import StudentSerializer, StudentSerializer01
from django.http import JsonResponse
from native_django.models import Student


# Create your views here.

class StudentView(View):
    def get2(self, request):
        """序列化器——序列化调用一条模型对象"""
        # 1.获取数据集
        student_list = Student.objects.first()
        # 2.实例化序列化器类，得到序列化对象
        serializer = StudentSerializer(instance=student_list)  # 序列化单个模型对象

        # 3.调用序列对象的data属性方法来获取对象
        data = serializer.data

        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    def get(self, request):
        """序列化器——序列化调用多个模型对象"""
        # 1.获取数据集
        student_list = Student.objects.all()
        # 2.实例化序列化器类，得到序列化对象 (多个模型对象必须声明many=True)
        serializer = StudentSerializer(instance=student_list, many=True)

        # 3.调用序列对象的data属性方法来获取对象
        data = serializer.data

        # 4.响应数据
        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})


class StudentView01(View):
    """反序列化，采用字段选项验证数据"""

    def post(self, request):
        # 1.接受客户端提交的数据
        post_data = request.POST
        print(post_data)
        data = {
            'name': post_data.get('name'),
            'age': post_data.get('age'),
            'sex': post_data.get('sex'),
            'classmate': post_data.get('classmate'),
            'description': post_data.get('description'),
        }
        # 1.1 实例化序列化器，获取序列化对象
        serializer = StudentSerializer01(data=data)
        # 1.2 调用序列化器进行数据验证 抛出异常，代码不继续执行
        serializer.is_valid(raise_exception=True)
        # 1.3 获取校验之后的结果
        return JsonResponse(dict(serializer.validated_data))

        # 2.操作数据库

        # 3.返回结果



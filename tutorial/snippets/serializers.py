# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 8:57 下午
@File ： serializers.py
@IDE  ： PyCharm
"""
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import generics

"""
创建一个序列化类
"""


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        给定验证过的数据创建并返回一个新的 Snippet 实例。
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据已验证的数据更新并返回已存在的 Snippet 实例。
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


# 使用ModelSerializers，创建序列化器类的快捷方式
class SnippetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class UserSericalizer(serializers.ModelSerializer):
    sinppets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meat:
        model = User
        fields = ('id', 'username', 'snippets')


"""
身份验证与权限
"""


class UserSerializer_Auth(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')  # 显式字段



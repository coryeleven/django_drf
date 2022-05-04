# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 16:19
# @Author  : Cory-小许同志
# @Email   :  coryeleven@foxmail.com


from rest_framework import serializers

"""
serializers 是drf 提供给开发者调用的序列化模块
Serializer  序列化基类，drf所有序列化器类都必须继承 Serializer
ModelSerializer 模型序列化基类，是序列化基类里面的子类，在工作中，除了Serializer之外，最常用的就是序列化器类基类
"""


class StudentSerializer(serializers.Serializer):
    """学生序列化器类"""
    # 1.转换的字段声明
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    classmate = serializers.CharField()
    description = serializers.CharField()

    # 2.如果序列化集成的是ModelSerializer,则需要声明调用的信息
    # 3.验证代码
    # 4.编写添加和更新模型的代码


class StudentSerializer01(serializers.Serializer):
    """学生序列化器类"""
    # 1.转换的字段声明,小括号里面的声明主要是给反序列化使用的
    id = serializers.IntegerField(read_only=True),  # 在客户端提交数据（反序列化阶段不要求id）
    name = serializers.CharField(required=True),  # 反序列化必填
    sex = serializers.BooleanField(default=True),  # 反序列化阶段，客户端没有提交，则默认为True
    age = serializers.IntegerField(max_value=100, min_value=0,
                                   error_messages={
                                       'max_value': 'The age failed must be age<=100',
                                       'min_value': 'The age failed must be age >= 0',
                                   }),
    classmate = serializers.CharField(max_length=100),
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)  # 允许客户端不填写内容，或者值为None

    # 2.如果序列化集成的是ModelSerializer,则需要声明调用的信息
    # 3.验证代码
    # 4.编写添加和更新模型的代码

    def validate_name(self, data):
        """验证单个字段
            方法名的格式必须以validate_<字段名>为名称，否则序列化不识别
            validate 开头的方法，会自动按is_valid 调用
        """
        print(data)
        if data in ['python', 'django']:
            return serializers.ValidationError(detail='学生姓名不能是python或django', code='validate_name')
        # 验证成功，必须返回data
        return data

    def validate(self, attrs):
        """
        验证来自客户端所有的数据
        validate 是固定的方法名
        参数: attrs,是在序列化实例化中的data选项数据
        """
        if attrs['sex'] and attrs['classmate'] == "307":
            raise serializers.ValidationError(detail='307班只能进去小姐姐～', code="validate")

        return attrs


def check_classmate(data):
    """外部验证函数"""
    if len(data) != 3:
        raise serializers.ValidationError(detail="班级格式不正确！必须是三个字符")
    # 验证完成，务必返回结果，否则最终的验证结果没有该数据
    return data

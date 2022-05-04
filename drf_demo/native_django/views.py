import json

from django.shortcuts import render
from django.views import View
from .models import Student
from django.http import JsonResponse

# Create your views here.

"""
post /students/ 添加一个学生信息
get /students/ 获取所有学生信息
get  /students/<pk> 获取一个学生信息
delete  /students/<pk> 删除一个学生信息
put  /students/ 更新一个学生信息


"""


class StudentView(View):
    """学生视图"""

    def post(self, request):
        """添加一个学生对象"""
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        classmate = request.POST.get('classmate')
        description = request.POST.get('description')

        instance = Student.objects.create(
            name=name,
            sex=sex,
            age=age,
            classmate=classmate,
            description=description,
        )

        return JsonResponse(data={
            "id": instance.pk,
            "name": instance.name,
            "sex": instance.sex,
            "age": instance.age,
            "classmate": instance.classmate,
            "description": instance.description,

        }, status=201)

    def get(self, request):
        """获取所有学生"""
        students = list(Student.objects.values())

        return JsonResponse(data=students, status=200, safe=False)


class StudentInfoView(View):
    def get(self, request, pk):
        """获取一条数据"""
        try:
            instance = Student.objects.get(pk=pk)
            return JsonResponse(data={
                "id": instance.pk,
                "name": instance.name,
                "sex": instance.sex,
                "age": instance.age,
                "classmate": instance.classmate,
                "description": instance.description,
            }, status=200)
        except Student.DoesNotExist:
            return JsonResponse(data=None, status=404)

    def put(self, request, pk):
        """修改学生信息"""
        result_resp = json.loads(request.body)
        print(result_resp)
        name = result_resp.get('name')
        sex = result_resp.get('sex')
        age = result_resp.get('age')
        classmate = result_resp.get('classmate')
        description = result_resp.get('description')

        try:
            instance = Student.objects.get(pk=pk)
            instance.name = name,
            instance.sex = sex,
            instance.age = age,
            instance.classmate = classmate,
            instance.description = description,
            instance.save()
        except Student.DoesNotExist:
            return JsonResponse(data=None, status=404)

        return JsonResponse(data={
            "id": instance.pk,
            "name": instance.name,
            "sex": instance.sex,
            "age": instance.age,
            "classmate": instance.classmate,
            "description": instance.description,

        }, status=201)

    def delete(self, request, pk):
        """删除一个学生"""
        try:
            Student.objects.filter(pk=pk).delete()
        except:
            pass
        return JsonResponse(data=None, status=204,safe=False)

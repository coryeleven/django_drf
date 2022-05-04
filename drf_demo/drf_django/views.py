from rest_framework.viewsets import ModelViewSet
from native_django.models import Student
from .serizlizers import StudentModelSerializers


# Create your views here.
# 视图集合
class StudentModelView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializers

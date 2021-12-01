import json

from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo


# Create your views here.
class BookInfoView(ModelViewSet):
    """列表视图"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

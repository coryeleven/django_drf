from django.shortcuts import render
from django.views import View


# Create your views here.

class BookListView(View):
    """列表视图"""

    def get(self, request):
        """查询所有图书接口"""
        pass

    def post(self, request):
        """新增图书接口"""
        pass


class BoolDetailView(View):
    """详情视图"""

    def get(self, request, pk):
        """查询指定某个图书接口"""
        pass

    def put(self, request, pk):
        """修改指定图书接口"""
        pass

    def delete(self, request, pk):
        """删除指定图书接口"""

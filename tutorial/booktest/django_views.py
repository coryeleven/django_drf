import json

from django.shortcuts import render
from django.views import View
from .models import BookInfo, HeroInfo
from django.http import JsonResponse, HttpResponse


# Create your views here.

class BookListView(View):
    """列表视图"""

    def get(self, request):
        """查询所有图书接口"""
        # 1.查询出所有图书的接口
        books = BookInfo.objects.all()
        # 2.遍历循环集，取出里面每个书籍的对象，把模型对象转换成字典
        # 定义一个列表，用来存储所有字典
        book_list = []
        for book in books:
            book_dict = {
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image if book.image else ''
            }
            book_list.append(book_dict)
            # 3.响应
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        """新增图书接口"""
        # 1.获取前段传入的请求体数据（json），request.body
        json_str_bytes = request.body
        # 2.把byte类型的json字符转换为json_str
        json_str = json_str_bytes.decode()
        # 3.利用json.loads 将字符串转换成json(字典/列表)
        book_dict = json.loads(json_str)
        # 4.创建模型对象并保存（把字典转换成模型对象并保存）
        book = BookInfo(
            btitle=book_dict['btitle'],
            bpub_date=book_dict['bpub_date']
        )
        book.save()
        # 5.响应(将新增的数据再响应回去)
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image if book.image else ''
        }
        return JsonResponse(book_dict, status=201)


class BookDetailView(View):
    """详情视图"""

    def get(self, request, pk):
        """查询指定某个图书接口"""
        # 1.获取指定pk的数据模型
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'msg': '查询的数据不存在'}, status=404)
        # 2.模型转字典
        book_dict = {
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image if book.image else ''
        }
        # 3.响应
        return JsonResponse(book_dict)

    def put(self, request, pk):
        """修改指定图书接口"""
        # 1.获取指定pk的数据模型
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'msg': '查询的数据不存在'}, status=404)
        # 2.获取前段传入的新数据
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        book_dict = json.loads(json_str)
        # 3.重新给模型指定的属性赋值
        book.btitle = book_dict['btitle']
        book.bpub_date = book_dict['bpub_date']
        # 4.调用save方法进行修改操作
        book.save()
        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image if book.image else ''
        }
        # 5.响应
        return JsonResponse(json_dict)

    def delete(self, request, pk):
        """删除指定图书接口"""
        # 1.获取要删除的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'msg': '查询的数据不存在'}, status=404)
        # 2.删除模型对象
        book.delete()  # 物理删除，真正从数据库中删除
        """
        # 逻辑删除
        book.is_delete = True
        book.save()
        """
        # 删除不需要指定响应体，但是指定状态为204
        return HttpResponse(status=204)

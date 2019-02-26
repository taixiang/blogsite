from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.decorators import api_view
import json
from .models import Blog, Me, Type
from django.core import serializers
from django.db.models import Count


class LoginApi(viewsets.ViewSet):
    def list(self, request):
        return Response(OrderedDict([
            ('code', 200),
            ('msg', "登录成功"),
            ('results', "1111")
        ]))


def api_result(code, msg, data=None):
    return Response(OrderedDict([
        ('code', code),
        ('msg', msg),
        ("data", data)
    ]))


def get_decorator(default_value):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return default_value

        return new_func

    return decorator


@get_decorator("登录失败")
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data['name']
        pwd = data['pwd']
        user = auth.authenticate(username=name, password=pwd)
        print(user)
        if user is not None:
            print(user.is_active)
            if user.is_active:
                auth.login(request, user)
            return api_result(200, "登录成功")
        else:
            return api_result(500, "登录失败")


# 首页
@get_decorator("网络异常")
@api_view()
def analyze(request):
    data = {}
    blog_list = []
    type_list = []
    blogs = Blog.objects.all().order_by("-count")
    blog_count = blogs.count()
    data["blog_count"] = blog_count
    total = 0
    for i, blog in enumerate(blogs):
        blog_tmp = {}
        blog_tmp["title"] = blog.title
        blog_tmp["count"] = blog.count
        blog_list.append(blog_tmp)
        total = total + blog.count
    data["total"] = total
    me = Me.objects.get(id=1)
    data["me_count"] = me.count
    data["blogs"] = blog_list
    types = Type.objects.annotate(num_blogs=Count("blog_post")).order_by("-num_blogs")
    for i, type in enumerate(types):
        type_tmp = {}
        type_tmp["name"] = type.name
        type_tmp["count"] = type.num_blogs
        type_list.append(type_tmp)
    data["types"] = type_list
    # datas = serializers.serialize("json", blogs)
    return api_result(200, "成功", data)


# 博客
@get_decorator("网络异常")
@api_view()
def blogs(request):
    data = {}
    blog_list = []
    blogs = Blog.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(blogs, 10)
    try:
        total = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        total = paginator.page(1)
    except EmptyPage:
        total = paginator.page(paginator.num_pages)
    if total.has_next():
        next = True
    else:
        next = False
    if total.has_previous():
        last = True
    else:
        last = False
    data["next"] = next
    data['last'] = last
    for i, blog in enumerate(total):
        blog_tmp = {}
        blog_tmp["title"] = blog.title
        blog_tmp["count"] = blog.count
        blog_tmp["id"] = blog.id
        blog_list.append(blog_tmp)
    data["blogs"] = blog_list
    data['total_page'] = paginator.num_pages
    return api_result(200, "成功", data)

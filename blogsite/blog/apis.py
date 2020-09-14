from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.decorators import api_view
import json
from .models import Blog, Me, Type, Shop, UserInfo, Marry
from django.core import serializers
from django.db.models import Count
import requests
from django.views.decorators.csrf import csrf_exempt
import time
from django.http import JsonResponse, HttpResponse


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


# 博客详情
@api_view()
def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    data = {}
    data["title"] = blog.title
    data["desc"] = blog.desc
    data["pub_time"] = blog.pub_time
    # data["md_file"] = blog.md_file
    # data["type_id"] = blog.type_id
    data["count"] = blog.count
    data["is_show"] = blog.is_show
    types = blog.type_id.all()
    type_list = []
    for type in types:
        type_tmp = {}
        type_tmp["name"] = type.name
        type_list.append(type.name)
    data["type"] = type_list

    # type = Type.objects.get(id=blog.pk)
    # data["type"] = type.name

    return api_result(200, "成功", data)


@api_view()
def foodList(request):
    data = {}
    shop = Shop.objects.all()
    shop_list = []
    for i, item in enumerate(shop):
        item_tmp = {}
        item_tmp["id"] = item.id
        item_tmp["name"] = item.name
        foods = item.food_set.all()
        food_list = []
        for j, food in enumerate(foods):
            food_tmp = {}
            food_tmp["id"] = food.id
            food_tmp["name"] = food.name
            food_tmp["num"] = food.num
            food_tmp["choose"] = food.isChoose
            food_tmp["remark"] = food.remark
            food_list.append(food_tmp)

        # food_json = serializers.serialize("json", foods)
        item_tmp["food"] = food_list
        # print(food_json)
        shop_list.append(item_tmp)
    data["list"] = shop_list
    return api_result(200, "成功", shop_list)


# 获取openid
def getOpenId(request):
    jscode = request.GET.get('code')
    print(jscode)
    print(111111)
    resp = requests.get(
        "https://api.weixin.qq.com/sns/jscode2session?appid=wx439a5d6962d0e1dc&secret=5081af1734a36ab72c2add3e934cdfdc&js_code=" + str(
            jscode) + "&grant_type=authorization_code")
    print(resp.text)
    # data = serializers.serialize("json", resp.text)
    return HttpResponse(json.dumps(resp.text), content_type="application/json")


# 用户信息保存
@csrf_exempt
def postUserInfo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(data)
        data['time'] = t
        print(data['openId'])
        user = UserInfo.objects.update_or_create(openId=data['openId'], defaults=data)[0]
        user.save()
    return JsonResponse(None, safe=False)


# 首页图片集合
@api_view()
def home_swiper(request):
    home_data = {
        'mainInfo': {
            'he': '邰祥',
            'she': '孙娟',
            'date': '10月24日',
            'lunar': '九月初八',
            'address': '姜堰区娄庄镇新龙村那旮旯'
        }
    }
    list = [
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/zhu1.jpg?sign=4496115c1ce17b097ec569d159fa08b8&t=1600005801',
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/xiuhe.jpg?sign=20af6488897108f69e62d3b7a323f85b&t=1600004835',
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/wai1.jpg?sign=6231f416a823262ee71593ece46c1a77&t=1600006469',
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/wai2.jpg?sign=ddd8b2ddc7076b9fc7236dcf58a6244f&t=1600006447',
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/xiaoyuan1.jpg?sign=6fd10c5c0885b0be49c764a2e34e642f&t=1600005512',
        'https://7765-wedding-i9l06-1303164777.tcb.qcloud.la/xiaoyuan2.jpg?sign=755e47cc7e4b88a0e6a2618d547da70c&t=1600006187']

    imgs = Marry.objects.all().filter(category_id=1)
    img_list = []
    for i,img in enumerate(imgs):
        img_list.append(img.img)

    home_data['img'] = img_list
    return api_result(200, "成功", home_data)

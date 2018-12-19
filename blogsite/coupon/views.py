# -*- coding:utf-8 -*-
import xlrd
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
import time

from django.views.decorators.csrf import csrf_exempt

import top
from .models import Coupon, Ques, Advice
import os
from django.conf import settings
import json


# markdown定位 去重
# Create your views here.
# 处理数据 类型+关键词
def query_data(keyword, type):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    keyword = keyword.replace(" ", "")
    name_dict = {}
    name_dict["name__contains"] = keyword
    type_dict = {}
    type_dict["type__contains"] = keyword
    shop_dict = {}
    shop_dict["shop__contains"] = keyword

    if type == "down":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).filter(
            Q(**name_dict) | Q(**type_dict) | Q(**shop_dict)).order_by("-price")
    elif type == "up":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).filter(
            Q(**name_dict) | Q(**type_dict) | Q(**shop_dict)).order_by('price')
    else:
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).filter(
            Q(**name_dict) | Q(**type_dict) | Q(**shop_dict)).order_by("-sale")

    return all_data


# 首页
def index(request):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).order_by("-sale")
    paginator = Paginator(all_data, 12)
    page = request.GET.get('page')
    s = request.GET.get('s')

    try:
        coupon_list = paginator.page(page)
    except PageNotAnInteger:
        coupon_list = paginator.page(1)
    except EmptyPage:
        coupon_list = paginator.page(paginator.num_pages)

    if coupon_list.has_next():
        has_next = True
    else:
        has_next = False

    # 二维码扫描
    if "qr" == s:
        ques = Ques.objects.all()
        first = ques[0]
        first.count_qr += 1
        first.save()

    return render(request, "coupon.html", {"coupon_list": coupon_list, "has_next": has_next})


# 好劵清单
def good_list(request):
    page = request.GET.get('page')
    keyword = request.GET["search"]
    keyword = keyword.replace(" ", "")
    try:
        page = int(page)
    except:
        page = 1
    print(keyword)
    req = top.api.TbkDgItemCouponGetRequest()
    req.set_app_info(top.appinfo("25102570", "a3bd49181cbecae30111cde7631ab5d6"))
    req.adzone_id = 43052050407
    req.platform = 2
    req.page_size = 12
    req.page_no = page
    req.q = keyword
    resp = req.getResponse()
    return JsonResponse(resp, safe=False)


# 好劵详情
def goods_detail(request):
    return render(request, "coupon_json.html")


# 选品库页面
def favorite(request, favorites_id):
    print(favorites_id)
    return render(request, "favorite_list.html", {"favorites_id": favorites_id})


# 选品库列表 18988664-母婴  18988609-女装
def favorites_list(request, favorites_id):
    page = request.GET.get('page')
    id = favorites_id
    try:
        page = int(page)
    except:
        page = 1
    req = top.api.TbkUatmFavoritesItemGetRequest()
    req.set_app_info(top.appinfo("25102570", "a3bd49181cbecae30111cde7631ab5d6"))

    req.platform = 2
    req.page_size = 12
    req.adzone_id = 43052050407
    req.favorites_id = id
    req.page_no = page
    req.fields = "num_iid,title,volume,zk_final_price,pict_url,coupon_info,shop_title,coupon_click_url,status,item_url"
    resp = req.getResponse()
    return JsonResponse(resp, safe=False)


# 猜你喜欢 暂时没有接口
def like(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    print(ip)
    page = request.GET.get('page')
    keyword = request.GET["search"]
    ua = request.GET.get('ua')
    net = request.GET["net"]
    os = request.GET.get('os')
    print(ua)
    print(net)
    print(os)

    req = top.api.TbkItemGuessLikeRequest()
    req.set_app_info(top.appinfo("25102570", "a3bd49181cbecae30111cde7631ab5d6"))

    req.adzone_id = 43052050407
    req.os = os
    req.ip = ip
    req.ua = ua
    req.net = net
    req.page_no = 1
    req.page_size = 20
    resp = req.getResponse()
    print(resp)
    return JsonResponse("{}", safe=False)


# 排序
def type_list(request, type):
    keyword = request.GET["search"]
    all_data = query_data(keyword, type)
    paginator = Paginator(all_data, 12)
    page = request.GET.get('page')

    try:
        coupon_list = paginator.page(page)
    except PageNotAnInteger:
        coupon_list = paginator.page(1)
    except EmptyPage:
        coupon_list = paginator.page(paginator.num_pages)

    if coupon_list.has_next():
        has_next = True
    else:
        has_next = False

    return render(request, "coupon.html",
                  {"coupon_list": coupon_list, "has_next": has_next, "type": type, "keyword": keyword})


# 更多
def more_coupon(request):
    type = request.GET.get('type')
    keyword = request.GET["search"]
    all_data = query_data(keyword, type)
    paginator = Paginator(all_data, 12)
    page = request.GET.get('page')
    try:
        coupon_list = paginator.page(page)
    except PageNotAnInteger:
        coupon_list = paginator.page(1)
    except EmptyPage:
        coupon_list = paginator.page(paginator.num_pages)

    if coupon_list.has_next():
        has_next = True
    else:
        has_next = False
    data = serializers.serialize("json", coupon_list)
    if coupon_list.has_next():
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"1\" }"
    else:
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"\" }"

    return JsonResponse(data, safe=False)


# 详情
def detail(request, coupon_id):
    detail_c = Coupon.objects.filter(uuid=coupon_id)
    detail = detail_c[0]
    detail.count += 1
    detail.save()
    return render(request, "coupon_detail.html", {"detail": detail})


# 搜索
def search(request):
    keyword = request.GET["search"]
    keyword = keyword.replace(" ", "")
    name_dict = {}
    name_dict["name__contains"] = keyword
    type_dict = {}
    type_dict["type__contains"] = keyword
    shop_dict = {}
    shop_dict["shop__contains"] = keyword

    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    all_data = Coupon.objects.filter(start_time__lte=cur_time, end_time__gte=cur_time).filter(
        Q(**name_dict) | Q(**type_dict) | Q(**shop_dict)).order_by("-sale")
    paginator = Paginator(all_data, 12)
    page = request.GET.get('page')

    try:
        coupon_list = paginator.page(page)
    except PageNotAnInteger:
        coupon_list = paginator.page(1)
    except EmptyPage:
        coupon_list = paginator.page(paginator.num_pages)

    if coupon_list.has_next():
        has_next = True
    else:
        has_next = False

    return render(request, "coupon.html", {"coupon_list": coupon_list, "has_next": has_next, "keyword": keyword})


# 口令生成
def create_key(request):
    text = request.GET["text"]
    url = request.GET["url"]
    logo = request.GET["logo"]
    req = top.api.TbkTpwdCreateRequest()
    req.set_app_info(top.appinfo("25102570", "a3bd49181cbecae30111cde7631ab5d6"))

    # req.user_id = "872592326"
    req.text = text
    req.url = url
    req.logo = logo
    # req.ext = "{}"
    resp = req.getResponse()
    return JsonResponse(resp, safe=None)


# 相关问题
def ques(request):
    ques = Ques.objects.all()
    first = ques[0]
    first.count += 1
    first.save()
    return render(request, "coupon_ques.html", {"msg": first})


# 意见反馈
@csrf_exempt
def post_advice(request):
    value = request.POST["value"]
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    advice = Advice(content=value, time=t)
    advice.save()
    return JsonResponse("{success}", safe=None)


# 删除文件
def deleteFile():
    media_root = os.path.join(settings.BASE_DIR, 'upload/excel/')
    for i in os.listdir(media_root):
        os.remove(media_root + i)


# 删除结束时间小于今日的
def delete_excel(request):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    coupon_list = Coupon.objects.filter(end_time__lt=cur_time)
    coupon_list.delete()
    return JsonResponse("{success}", safe=False)


# 先写入数据库，同时删除excel文件
def word_create(request):
    goods_list = []
    media_root = os.path.join(settings.BASE_DIR, 'upload/excel/')
    word_path = media_root + "coupon.xls"
    workbook = xlrd.open_workbook(word_path)
    sheet = workbook.sheet_by_index(0)
    v_1 = sheet.row_values(0)
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    for i in range(1, sheet.nrows):
        v = sheet.row_values(i)
        if v[19] >= cur_time >= v[18]:
            goods_list.append(v)
    # 佣金排序
    goods_list.sort(key=lambda x: float(x[9]), reverse=True)
    for i in goods_list:
        coupon = Coupon()
        coupon.uuid = i[0]
        coupon.name = i[1]
        coupon.img = i[2]
        coupon.type = i[4]
        coupon.detail_url = i[5]
        coupon.price = i[6]
        coupon.sale = i[7]
        coupon.money = i[9]
        coupon.shop = i[12]
        if i[13] == "淘宝":
            coupon.platform = 1
        elif i[13] == "天猫":
            coupon.platform = 2
        coupon.rule = i[17]
        coupon.start_time = i[18]
        coupon.end_time = i[19]
        coupon.web_url = i[20]
        coupon.phone_url = i[21]
        coupon.save()
    deleteFile()
    return JsonResponse("{success}", safe=False)


# 删除所有数据
def delete_all(request):
    coupon_list = Coupon.objects.all()
    coupon_list.delete()
    return JsonResponse("{success}", safe=False)

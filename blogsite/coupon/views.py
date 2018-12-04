from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
import time
from .models import Coupon


# Create your views here.
def index(request):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time)
    paginator = Paginator(all_data, 10)
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

    return render(request, "coupon.html", {"coupon_list": coupon_list, "has_next": has_next})


def type_list(request, type):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(cur_time)
    if type == "down":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).order_by("-price")
    elif type == "up":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).order_by('price')
    else:
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time)
    paginator = Paginator(all_data, 10)
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

    return render(request, "coupon.html", {"coupon_list": coupon_list, "has_next": has_next, "type": type})


def more_coupon(request):
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    type = request.GET.get('type')
    if type == "down":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).order_by("-price")
    elif type == "up":
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time).order_by('price')
    else:
        all_data = Coupon.objects.filter(start_time__lte=cur_time).filter(end_time__gte=cur_time)
    paginator = Paginator(all_data, 10)
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


def detail(request, coupon_id):
    detail_c = Coupon.objects.filter(uuid=coupon_id)
    return render(request, "coupon_detail.html", {"detail": detail_c[0]})


def delete_excel(request):
    return render(request, "coupon.html")

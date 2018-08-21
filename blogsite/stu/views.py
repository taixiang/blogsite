from django.shortcuts import render
from .models import StuImg
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    # forloop.counter
    imgs = StuImg.objects.all()
    paginator = Paginator(imgs, 9)
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    if data.has_next():
        print("============")
        has_next = True
    else:
        has_next = False
    return render(request, "stu.html", {"imgs": data, "has_next": has_next})


def moreImg(request):
    page = request.GET.get('page')
    customer = StuImg.objects.all()
    paginator = Paginator(customer, 9)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    data = serializers.serialize("json", customer)
    if customer.has_next():
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"1\" }"
    else:
        data = "{ \"data\":" + data + ",\"page\":" + page + ",\"next\":\"\" }"
    return JsonResponse(data, safe=False)


def count(request):
    id = request.GET.get("id")
    img = StuImg.objects.get(pk=id)
    img.count += 1
    img.save()
    return JsonResponse(None, safe=False)
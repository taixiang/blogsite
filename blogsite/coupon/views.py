from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from .models import Coupon


# Create your views here.
def index(request):
    all_data = Coupon.objects.all()
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
    print("========")
    print(type)
    all_data = Coupon.objects.all()
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


def delete_excel(request):
    return render(request, "coupon.html")

from django.shortcuts import render
from .models import Coupon


# Create your views here.
def index(request):
    coupon_list = Coupon.objects.all()
    return render(request, "coupon.html", {"coupon_list": coupon_list,"test":"11"})


def delete_excel(request):
    return render(request, "coupon.html")

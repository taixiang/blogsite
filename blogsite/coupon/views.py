from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"coupon.html")

def delete_excel(request):
    return render(request, "coupon.html")
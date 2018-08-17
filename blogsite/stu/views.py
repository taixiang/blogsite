from django.shortcuts import render
from .models import StuImg


# Create your views here.

def index(request):
    # forloop.counter
    imgs = StuImg.objects.all()
    print(imgs)
    return render(request, "stu.html", {"imgs": imgs})

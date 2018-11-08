from django.db.models import Count
from django.shortcuts import render
from .models import Blog, Type, Me, Ascii
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from PIL import Image
import os
from django.http import HttpResponseRedirect
from django.conf import settings
from . import randomcode


# Create your views here.


def index(request):
    me = Me.objects.all()
    blogs = Blog.objects.all().filter(is_show=0)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    if customer.has_next():
        has_next = True
    else:
        has_next = False
    return render(request, "index.html", {"blogs": customer, "cur_page": page, "has_next": has_next, "msg": me[0]})


def detail(request, blog_id):
    me = Me.objects.all()
    detail = Blog.objects.get(id=blog_id)
    detail.count += 1
    detail.save()
    return render(request, "detail.html", {"detail": detail, "msg": me[0]})


def archive(request):
    me = Me.objects.all()
    blogs = Blog.objects.all().filter(is_show=0)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    return render(request, "archive.html", {"blogs": customer, "count": blogs.count(), "msg": me[0]})


def category(request):
    me = Me.objects.all()
    categorys = Type.objects.all()
    t = Type.objects.annotate(num_blogs=Count("blog_post"))
    return render(request, "category.html", {"categorys": t, "count": categorys.count(), "msg": me[0]})


def category_detail(request, type_id):
    me = Me.objects.all()
    type = Type.objects.all().get(id=type_id)
    blogs = Blog.objects.all().filter(type_id=type_id, is_show=0)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request, "category_detail.html", {"blogs": customer, "type": type.name, "msg": me[0]})


def category_name(request):
    me = Me.objects.all()
    type = Type.objects.all().get(name="彩蛋")
    blogs = Blog.objects.all().filter(type_id=type.id, is_show=0)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request, "category_detail.html", {"blogs": customer, "type": type.name, "msg": me[0]})


def about(request):
    me = Me.objects.all()
    me_first = me[0]
    me_first.count += 1
    me_first.save()
    return render(request, "about.html", {"msg": me[0]})


# 字符画
def post_img(request):
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    print(media_root)
    if request.method == "POST":
        img = request.FILES.get('img')
        if img is not None:
            width = int(request.POST["width"])
            if width <= 0:
                width = 80
            height = int(request.POST["height"])
            if height <= 0:
                height = 60
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            ascii = Ascii(img=img, time=t)
            # print("============")
            ascii.save()
            im = Image.open(media_root + str(ascii.img))
            im = im.resize((width, height), Image.NEAREST)
            txt = ""

            sub_txt_name = str(ascii.id) + ".txt"
            txt_name = media_root + "txt/" + sub_txt_name
            for i in range(height):
                for j in range(width):
                    txt += get_char(*im.getpixel((j, i)))
                txt += '\n'
            with open(txt_name, 'w') as f:
                f.write(txt)
            if settings.DEBUG:
                url = "http://127.0.0.1:8000/upload/txt/" + sub_txt_name
            else:
                url = "https://www.manjiexiang.cn/upload/txt/" + sub_txt_name

            return HttpResponseRedirect(url)
        else:
            me = Me.objects.all()
            return render(request, "ascii.html", {"msg": me[0]})
    else:
        me = Me.objects.all()
        return render(request, "ascii.html", {"msg": me[0]})


# 验证码
def validate_code(request):
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    img_name = media_root + "img/pic.png"
    print(media_root)
    randomcode.createImg(img_name)
    if settings.DEBUG:
        url = "http://127.0.0.1:8000/upload/img/pic.png"
    else:
        url = "https://www.manjiexiang.cn/upload/img/pic.png"
    return render(request, "validate.html", {"img": url})


def get_char(r, g, b, alpha=256):
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def get_root(request):
    return render(request, "root.txt")

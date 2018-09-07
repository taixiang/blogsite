from django.db.models import Count
from django.shortcuts import render
from .models import Blog, Type, Me, Ascii
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from PIL import Image
import os
from django.conf import settings
from django.http import FileResponse
import threading


# Create your views here.


def index(request):
    me = Me.objects.all()
    blogs = Blog.objects.all()
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
    blogs = Blog.objects.all()
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
    blogs = Blog.objects.all().filter(type_id=type_id)
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
                height = 80
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            ascii = Ascii(img=img, time=t)
            # print("============")
            ascii.save()
            print(ascii.img)
            im = Image.open(media_root + str(ascii.img))
            im = im.resize((width, height), Image.NEAREST)
            txt = ""
            txt_name = str(ascii.id) + ".txt"
            for i in range(height):
                for j in range(width):
                    txt += get_char(*im.getpixel((j, i)))
                txt += '\n'
            with open(txt_name, 'w') as f:
                f.write(txt)

            file = open(txt_name, 'rb')
            response = FileResponse(file)

            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % txt_name
            try:
                return response
            finally:
                # file.close()
                # os.remove(txt_name)
                # time.sleep(0.5)
                # return render(request, "ascii.html")
                pass
                # os.remove(txt_name)
                # return render(request, "ascii.html")
        else:
            return render(request, "ascii.html")
    else:
        return render(request, "ascii.html")


def get_char(r, g, b, alpha=256):
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

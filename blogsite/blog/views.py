from django.db.models import Count
from django.shortcuts import render
from .models import Blog, Type
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)
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
    return render(request, "index.html", {"blogs": customer, "cur_page": page, "has_next": has_next})


def detail(request, blog_id):
    detail = Blog.objects.get(id=blog_id)
    return render(request, "detail.html", {"detail": detail})


def archive(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    return render(request, "archive.html", {"blogs": customer, "count": blogs.count()})


def category(request):
    categorys = Type.objects.all()
    t = Type.objects.annotate(num_blogs=Count("blog_post"))
    return render(request, "category.html", {"categorys": t, "count": categorys.count()})


def category_detail(request, type_id):
    type = Type.objects.all().get(id=type_id)
    blogs = Blog.objects.all().filter(type_id=type_id)
    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request, "category_detail.html", {"blogs": customer, "type": type.name})

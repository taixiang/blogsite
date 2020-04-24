from django.db.models import Count
from django.shortcuts import render
from .models import Blog, Type, Me, Ascii, wordhtml
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
from PIL import Image
import os
from django.http import HttpResponseRedirect
from django.conf import settings
from . import randomcode
import shortuuid
from pydocx import PyDocX
import xlrd


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


# 杂谈
def talk(request):
    return render(request, "talk.html")


# agent
def agent(request):
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    me = Me.objects.all()
    msg = me[0]
    path = media_root + str(msg.excel_ag)

    names_ag = ['许亮', '朱涵威', '高永柳', '彭玲', '王都胜',
                '赵玮', '王锐健', '袁艺', '张凯', '薛飞',
                '曲虎鹏', '徐星', '赵俊', '冯美子', '黄春贞',
                '马云凤', '李武龙', '马光旭', '朴永鹤', '王惠娟',
                '王启超', '谢佳', '马丙强', '林雨彬', '杨洁',
                '张泽鹏', '樊杰', '赵志军', '赵吉', '段永菊',
                '葛杨', '田晨', '王南', '王瑶', '赵启霞',
                '黄新雨', '林炳炎', '王海靖', '方建兵', '赵兵',
                '张云',
                '赵晨浩', '任芮', '豆永坤', '吴孝辰', '张健',
                '张宁', '张艳梅', '朱秀国', '陈海涛', '林雨鸿',
                '曲晓伟', '庄强', '吴燕', '施涛', '王锡利',
                '高盖', '王成', '吕迎春', '芮金根', '葛磊',
                '王赛', '朱云霞', '胡楠', '万小林', '张宝云',
                '张敏', '朱玲', '徐家文', '刘卫华', '赵毅',
                '王丽娜', '周虹', '张都帅', '朱宗旺', '张光军',
                '朱丽萍', '吴亚军', '黄瓒', '吴雪利', '张贞芳',
                '赵敬阳', '戎孟雨', '邵明远', '徐泓达', '王先文',
                '王启龙', '邰祥', '徐西珍', '江翠', '周谦',
                '戴丽', '吴小宝', '韦家志', '朱素兰', '王俊菲',
                '杜金河', '王亚飞', '杨孟雅', '胡金芝', '刘凯',
                '蔡梦', '刘胜杰', '王楠', '张鑫', '朱倩媛',
                '袁野', '赵伟方', '娄玉', '刘鹏', '赵宁宁',
                '董兴辉', '张越', '朱庆义', '樊晓兵', '绳凤',
                '王刚',
                '樊秋茹', '彭正聪', '王键', '张峰华', '肖双娥',
                '孙波', '陈勇', '董国荣', '段元通']
    moneys_ag = []
    data_ag = []
    excel = xlrd.open_workbook(str(path))
    excel.sheet_names()
    sheet = excel.sheet_by_index(0)
    names = sheet.col_values(2)
    money = sheet.col_values(9)
    for i in range(0, sheet.nrows):
        # 表格里的数据
        name = sheet.cell(i, 2).value
        if name in names_ag:
            data = (name, (float)(sheet.cell(i, 9).value))
            print(type(data))
            data_ag.append(data)

    new_data_ag = sorted(data_ag, key=lambda s: s[1], reverse=True)
    last_ag = new_data_ag[-20:]
    time = msg.pub_time

    return render(request, "agent.html", {"last_ag": last_ag, "time": time, "msg": me[0]})


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
    me = Me.objects.all()
    id = shortuuid.uuid()
    img_name = str(id) + ".png"
    img_path = media_root + "img/" + img_name
    print(media_root)
    randomcode.createImg(img_path)
    if settings.DEBUG:
        url = "http://127.0.0.1:8000/upload/img/" + img_name
    else:
        url = "https://www.manjiexiang.cn/upload/img/" + img_name
    return render(request, "validate.html", {"img": url, "msg": me[0]})


# word转html
def wordtohtml(request):
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    if request.method == "POST":
        file = request.FILES.get('file')
        if file is not None:
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            id = shortuuid.uuid()
            word = wordhtml(word=file, time=t, uuid=id)
            word.save()
            file_path = media_root + str(word.word)
            html = PyDocX.to_html(file_path)
            html_name = str(word.uuid) + ".html"
            txt_name = media_root + "word/" + html_name
            f = open(txt_name, 'w', encoding="utf-8")
            f.write(html)
            f.close()
            if settings.DEBUG:
                url = "http://127.0.0.1:8000/upload/word/" + html_name
            else:
                url = "https://www.manjiexiang.cn/upload/word/" + html_name
            return HttpResponseRedirect(url)
        else:
            me = Me.objects.all()
            return render(request, "wordtohtml.html", {"msg": me[0]})
    else:
        me = Me.objects.all()
        return render(request, "wordtohtml.html", {"msg": me[0]})


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


def get_wx_root(request):
    return render(request, "MP_verify_cFL29g0dxlethL6n.txt")

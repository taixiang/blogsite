from django.db.models import Count
from django.shortcuts import render
from .models import Blog, Type, Me, Ascii, wordhtml, WxToken, JsToken
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
import json
import requests
import uuid
import random
import string
from django.utils import timezone
import hashlib


# Create your views here. https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET


def getJsApiTicket():
    # 获得jsapi_ticket
    # 获得jsapi_ticket之后，就可以生成JS-SDK权限验证的签名了
    # 获取access_token
    try:
        ticket = WxToken.objects.all()[0]
        if ticket.get_date():
            return ticket.token
    except:
        ticket = WxToken()

    accessToken = accesstokens()

    # 获取jsapi_ticket
    url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=' + accessToken + '&type=jsapi'
    jsapiReq = requests.get(url)

    jsapi = json.loads(jsapiReq.text)
    jsapi_ticket = jsapi['ticket']

    ticket.token = str(jsapi_ticket)
    ticket.lifetime = timezone.now()
    ticket.save()
    print('--------jsapi_ticket---------')
    print(jsapi_ticket)
    return str(jsapi_ticket)


def accesstokens():
    try:
        accesstoken = JsToken.objects.all()[0]
        if accesstoken.get_date():
            return accesstoken.token
    except:
        accesstoken = JsToken()

    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx2591758bb5b63c70&secret=1db783ec4e6715bd9b9c2577f198b4c3'

    resp = requests.get(url)
    token_json = json.loads(resp.text)
    # print(token_json['access_token'])
    ACCESS_TOKEN = token_json['access_token']

    accesstoken.token = ACCESS_TOKEN
    accesstoken.lifetime = timezone.now()
    accesstoken.save()
    print('--------ACCESS_TOKEN---------')
    print(ACCESS_TOKEN)
    return ACCESS_TOKEN


def createNonceStr(length=16):
    # 获取noncestr（随机字符串）
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


def index(request):
    # 获得jsapi_ticket
    jsapiTicket = getJsApiTicket()
    # 注意 URL 一定要动态获取，不能 hardcode.
    # 获取当前页面的url
    url = 'https://' + request.get_host() + request.get_full_path()

    # 获取timestamp（时间戳）
    timestamp = int(time.time())
    # 获取noncestr（随机字符串）
    nonceStr = createNonceStr()

    # 这里参数的顺序要按照 key 值 ASCII 码升序排序
    # 得到signature
    # $signature = hashlib.sha1(string).hexdigest();
    ret = {
        'nonceStr': nonceStr,
        'jsapi_ticket': jsapiTicket,
        'timestamp': timestamp,
        'url': url
    }

    string = '&'.join(['%s=%s' % (key.lower(), ret[key]) for key in sorted(ret)])
    signature = hashlib.sha1(string.encode("utf8")).hexdigest()

    signPackage = {
        "appId": 'wx2591758bb5b63c70',
        "nonceStr": nonceStr,
        "timestamp": timestamp,
        "url": url,
        "signature": signature,
        "rawString": string
    }

    print(signPackage)

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
    return render(request, "index.html", {"blogs": customer, "cur_page": page, "has_next": has_next, "msg": me[0], "obj":signPackage})


# 杂谈
def talk(request):
    return render(request, "talk.html")


# agent
def agent(request):
    me = Me.objects.all()
    msg = me[0]
    agent_data = msg.agent_data
    all_data = json.loads(agent_data)

    ag_num = msg.ag_num
    last_ag = all_data[-ag_num:]
    time = msg.pub_time

    return render(request, "agent.html", {"last_ag": last_ag, "time": time, "ag_num": ag_num, "msg": me[0]})


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


# marry
def marry(request):
    return render(request, "marry.html")

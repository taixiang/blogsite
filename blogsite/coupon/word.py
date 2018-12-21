import hashlib
import json
import random
import string

import requests
import xlrd
import time
import os
import django
from django.conf import settings
import top.api

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogsite.settings")
django.setup()
from coupon.models import Coupon


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[9]


# 删除文件
def deleteFile():
    media_root = os.path.join(settings.BASE_DIR, 'upload/excel/')
    for i in os.listdir(media_root):
        os.remove(media_root + i)


def word():
    goods_list = []
    media_root = os.path.join(settings.BASE_DIR, 'upload/excel/')
    word_path = media_root + "2.xls"
    workbook = xlrd.open_workbook(word_path)
    sheet = workbook.sheet_by_index(0)
    v_1 = sheet.row_values(0)
    print(v_1)
    cur_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(cur_time)

    for i in range(1, sheet.nrows):
        v = sheet.row_values(i)
        if v[19] >= cur_time >= v[18]:
            goods_list.append(v)
    # 佣金排序
    goods_list.sort(key=lambda x: float(x[9]), reverse=True)
    for i in goods_list:
        coupon = Coupon()
        coupon.uuid = i[0]
        coupon.name = i[1]
        coupon.img = i[2]
        coupon.type = i[4]
        coupon.detail_url = i[5]
        coupon.price = i[6]
        coupon.money = i[9]
        coupon.shop = i[12]
        if i[13] == "淘宝":
            coupon.platform = 1
        elif i[13] == "天猫":
            coupon.platform = 2
        coupon.rule = i[17]
        coupon.start_time = i[18]
        coupon.end_time = i[19]
        coupon.web_url = i[20]
        coupon.phone_url = i[21]
        coupon.save()
    deleteFile()


def key():
    req = top.api.TbkTpwdCreateRequest()
    req.set_app_info(top.appinfo("25102570", "a3bd49181cbecae30111cde7631ab5d6"))

    req.user_id = "123"
    req.text = "长度大于5个字符"
    req.url = "https://uland.taobao.com/"
    req.logo = "https://uland.taobao.com/"
    req.ext = "{}"
    resp = req.getResponse()
    print(resp)


def get_access_token():
    resp = requests.get(
        "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx2591758bb5b63c70&secret=1db783ec4e6715bd9b9c2577f198b4c3")
    token = json.loads(resp.text)
    resp = requests.get(
        "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=" + token["access_token"] + "&type=jsapi")
    print(resp.text)


# get_access_token()

def create_nonce_str():
    noncestr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    timestamp = int(time.time())
    _jsapi_ticket = "jsapi_ticket"
    _noncestr = "&noncestr=" + noncestr
    _timestamp = "&timestamp="+ str(timestamp)
    _url = "&url=https://www.manjiexiang.cn/youhui"
    all_str = _jsapi_ticket + _noncestr + _timestamp + _url
    print(all_str.encode("UTF-8"))
    sha1 = hashlib.sha1(all_str.encode('utf8')).hexdigest()
    print(sha1)

create_nonce_str()

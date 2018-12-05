import xlrd
import time
import os
import django
from django.conf import settings

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

word()
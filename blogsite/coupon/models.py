from django.db import models
from django.utils import timezone

platform_type = ((1, "淘宝"), (2, "天猫"))


# Create your models here.
class Coupon(models.Model):
    uuid = models.CharField("商品id", blank=True, default="", max_length=40)
    name = models.CharField("商品名称", blank=True, default="", max_length=200)
    img = models.CharField("商品主图", blank=True, default="", max_length=200)
    type = models.CharField("商品类别", blank=True, default="", max_length=50)
    detail_url = models.TextField("淘宝客链接", blank=True, default="")
    price = models.DecimalField("商品价格", blank=True, max_digits=7, decimal_places=2)
    sale = models.IntegerField("销量", default=0)
    money = models.CharField("佣金", blank=True, default="", max_length=10)
    shop = models.CharField("店铺", blank=True, default="", max_length=50)
    platform = models.IntegerField("平台", choices=platform_type, blank=True, default=0)
    rule = models.CharField("优惠券面额", blank=True, default="", max_length=50)
    start_time = models.CharField("开始时间", blank=True, default="", max_length=20)
    end_time = models.CharField("结束时间", blank=True, default="", max_length=20)
    web_url = models.TextField("pc", blank=True, default="")
    phone_url = models.TextField("phone", blank=True, default="")
    count = models.IntegerField("次数", default=0)

    class Meta:
        verbose_name = "优惠券"
        verbose_name_plural = "优惠券"

    def __str__(self):
        return self.name


# excel
class Word(models.Model):
    word = models.FileField("word", upload_to='excel/', blank=True)
    pub_time = models.DateTimeField("时间", default=timezone.now)

    def __str__(self):
        return "test"


# 意见反馈
class Advice(models.Model):
    content = models.TextField("意见反馈", blank=True, default="")
    time = models.CharField("时间", max_length=150, blank=True, default="")

    class Meta:
        verbose_name = "意见反馈"
        verbose_name_plural = "意见反馈"
        ordering = ["-time"]


# md文件
class Ques(models.Model):
    about_me = models.FileField("相关问题", upload_to='file/%Y/%m/%d/', blank=True)
    count = models.IntegerField("次数", default=0)

    def __str__(self):
        return "相关问题"

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
    price = models.CharField("商品价格", blank=True, default="", max_length=10)
    money = models.CharField("佣金", blank=True, default="", max_length=10)
    shop = models.CharField("店铺", blank=True, default="", max_length=50)
    platform = models.IntegerField("平台", choices=platform_type, blank=True, default=0)
    rule = models.CharField("优惠券面额", blank=True, default="", max_length=50)
    start_time = models.CharField("开始时间", blank=True, default="", max_length=20)
    end_time = models.CharField("结束时间", blank=True, default="", max_length=20)
    web_url = models.TextField("pc", blank=True, default="")
    phone_url = models.TextField("phone", blank=True, default="")

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

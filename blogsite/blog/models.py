from django.db import models
from django.utils import timezone


# Create your models here.
class Type(models.Model):
    name = models.CharField("类别", max_length=40)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    order = models.IntegerField("权重值", default=0)

    class Meta:
        ordering = ["-order"]
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField("标题", max_length=150)
    desc = models.TextField("描述")
    pub_time = models.DateTimeField("时间", default=timezone.now)
    md_file = models.FileField("文件", upload_to='file/%Y/%m/%d/', blank=True)
    type_id = models.ManyToManyField("type", related_name="blog_post", verbose_name="分类")
    count = models.IntegerField("次数", default=0)

    class Meta:
        ordering = ["-pub_time"]

    def __str__(self):
        return self.title


class Me(models.Model):
    name = models.CharField("昵称", max_length=150)
    avatar = models.ImageField("头像", upload_to='file/%Y/%m/%d/', blank=True)
    qr_code = models.ImageField("二维码", upload_to='file/%Y/%m/%d/', blank=True)
    about_me = models.FileField("关于我", upload_to='file/%Y/%m/%d/', blank=True)
    zan = models.ImageField("赞赏", upload_to='file/%Y/%m/%d/', blank=True)
    juejin = models.CharField("掘金", max_length=150)
    zhihu = models.CharField("知乎", max_length=150)
    jianshu = models.CharField("简书", max_length=150)
    count = models.IntegerField("次数", default=0)

    def __str__(self):
        return self.name


# 字符码
class Ascii(models.Model):
    img = models.ImageField("图片", upload_to='file/%Y/%m/%d/', blank=True)
    pub_time = models.DateTimeField("时间", default=timezone.now)
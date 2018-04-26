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

    class Meta:
        ordering = ["-pub_time"]

    def __str__(self):
        return self.title

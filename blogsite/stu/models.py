from django.db import models
from django.utils import timezone


# Create your models here.
class StuImg(models.Model):
    title = models.CharField("标题", max_length=50, default="", blank=True)
    img = models.ImageField("图片", upload_to="photos/%Y/%m/%d")
    count = models.IntegerField("", default=0)
    order = models.IntegerField("排序权重", default=0, help_text="值越大越靠前")
    pub_time = models.DateTimeField("时间", default=timezone.now)

    class Meta:
        ordering = ["-order", "pub_time"]
        verbose_name = "照片列表"
        verbose_name_plural = "照片列表"

    def image(self):
        return '<img src="/upload/%s" width="60px" height="60px" />' % self.img

    image.allow_tags = True
    image.short_description = "图片"

    def __str__(self):
        return self.title

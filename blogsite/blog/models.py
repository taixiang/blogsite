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
    is_show = models.IntegerField("显示", default=0)

    class Meta:
        ordering = ["-pub_time"]

    def __str__(self):
        return self.title


class Me(models.Model):
    name = models.CharField("昵称", max_length=150)
    avatar = models.ImageField("头像", upload_to='file/%Y/%m/%d/', blank=True)
    qr_code = models.ImageField("二维码", upload_to='file/%Y/%m/%d/', blank=True)
    about_me = models.FileField("关于我", upload_to='file/%Y/%m/%d/', blank=True)
    excel_ag = models.FileField("excel", upload_to='file/%Y/%m/%d/', blank=True)
    zan = models.ImageField("赞赏", upload_to='file/%Y/%m/%d/', blank=True)
    juejin = models.CharField("掘金", max_length=150)
    zhihu = models.CharField("知乎", max_length=150)
    jianshu = models.CharField("简书", max_length=150)
    count = models.IntegerField("次数", default=0)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    ag_num = models.IntegerField("ag数量", default=0)
    agent_data = models.TextField("结果", default='', blank=True)

    def __str__(self):
        return self.name


# 字符码
class Ascii(models.Model):
    img = models.ImageField("图片", upload_to='postimg/', blank=True)
    time = models.CharField("时间", max_length=150, blank=True, default="")

    def image(self):
        return '<img src="/upload/%s" width="100px" height="100px" />' % self.img

    image.allow_tags = True
    image.short_description = "图片"

    def __str__(self):
        return self.time


# word转html
class wordhtml(models.Model):
    word = models.FileField("word", upload_to='word/', blank=True)
    time = models.CharField("时间", max_length=150, blank=True, default="")
    uuid = models.CharField("uuid", max_length=50, blank=True, default="")

    def __str__(self):
        return self.uuid


# -----------------------------------

# 用户表
class UserInfo(models.Model):
    nickName = models.CharField("昵称", max_length=150, blank=True, default="")
    avatarUrl = models.TextField("头像", blank=True, default="")
    gender = models.IntegerField("性别", blank=True, default=0)
    language = models.CharField("语言", max_length=150, blank=True, default="")
    city = models.CharField("市", max_length=150, blank=True, default="")
    province = models.CharField("省", max_length=150, blank=True, default="")
    country = models.CharField("国家", max_length=150, blank=True, default="")
    openId = models.CharField("openId", max_length=150, blank=True, default="", unique=True)
    time = models.CharField("时间", max_length=150, blank=True, default="")

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = "用户列表"

    def __str__(self):
        return self.nickName


# 商户
class Shop(models.Model):
    name = models.CharField("商家", max_length=50, blank=True, default="")

    class Meta:
        verbose_name = "商户"
        verbose_name_plural = "商户"

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField("商品", max_length=50, blank=True, default="")
    isChoose = models.BooleanField("是否数量选择")
    num = models.CharField("数量选择(2个|4个 格式)", max_length=150, blank=True, default="")
    remark = models.CharField("备注", max_length=150, blank=True, default="")
    shop_id = models.ForeignKey(Shop, blank=True, default="")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return self.name


class FoodOrder(models.Model):
    user_id = models.ForeignKey(UserInfo, to_field="openId", blank=True, default="")
    time = models.CharField("时间", max_length=150, blank=True, default="")
    name = models.CharField("商品", max_length=50, blank=True, default="")
    isChoose = models.BooleanField("是否数量选择")
    num = models.CharField("数量选择(2个|4个 格式)", max_length=150, blank=True, default="")
    remark = models.CharField("备注", max_length=150, blank=True, default="")

    class Meta:
        verbose_name = "商品订单"
        verbose_name_plural = "商品订单"

    def __str__(self):
        return self.name

# ------------------------------------------------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField("类别", max_length=40)
    img = models.CharField("图片", max_length=200, default="", blank=True)
    desc = models.CharField("描述", max_length=100, default="", blank=True)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    order = models.IntegerField("权重值", default=0, help_text="值越大越靠前")
    is_show = models.IntegerField("显示", default=1)

    class Meta:
        ordering = ["-order", "pub_time"]
        verbose_name = "图片分类"
        verbose_name_plural = "图片分类"

    def __str__(self):
        return self.name

# 图片
class Marry(models.Model):
    name = models.CharField("名称", max_length=40, default="", blank=True)
    img = models.CharField("图片", max_length=200, default="", blank=True)
    desc = models.CharField("描述", max_length=100, default="", blank=True)
    order = models.IntegerField("权重值", default=0, help_text="值越大越靠前")
    pub_time = models.DateTimeField("时间", default=timezone.now)
    category_id = models.ManyToManyField("Category", related_name="marry_post", verbose_name="分类", blank=True)
    is_h = models.IntegerField("是否横向", default=0)

    class Meta:
        ordering = ["-order", "pub_time"]
        verbose_name = "图片列表"
        verbose_name_plural = "图片列表"

    def image(self):
        return '<img src="/upload/img/%s" width="60px" height="60px" />' % self.img1

    image.allow_tags = True
    image.short_description = "图片"

    def __str__(self):
        return self.name

class JoinMsg(models.Model):
    name = models.CharField("姓名", max_length=40, default="", blank=True)
    phone = models.CharField("手机号", max_length=20, default="", blank=True)
    msg = models.CharField("出席信息", max_length=10, default="", blank=True)
    remark = models.CharField("备注", max_length=100, default="", blank=True)
    openId = models.CharField("openId", max_length=150, blank=True, default="")
    time = models.CharField("时间", max_length=150, blank=True, default="")

    class Meta:
        verbose_name = "出席信息"
        verbose_name_plural = "出席信息"

    def __str__(self):
        return self.name


class WxToken(models.Model):
    token = models.CharField(max_length=200)
    lifetime = models.DateTimeField(
        default=0
    )

    def get_date(self):
        delta = timezone.now() - self.lifetime
        if delta.seconds < 6000:
            return True
        else:
            return False


class JsToken(models.Model):
    token = models.CharField(max_length=200)
    lifetime = models.DateTimeField(
        default=0
    )

    def get_date(self):
        delta = timezone.now() - self.lifetime
        if delta.seconds < 6000:
            return True
        else:
            return False

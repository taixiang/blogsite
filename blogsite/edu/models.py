from django.db import models
from django.utils import timezone

class_type = ((1, "小学"), (2, "初中"))


# Create your models here.
class ClassType(models.Model):
    name = models.CharField("年级", max_length=20)
    order = models.IntegerField("权重值", default=0)
    pub_time = models.DateTimeField("时间", default=timezone.now)

    class Meta:
        ordering = ["-order"]
        verbose_name = "年级"
        verbose_name_plural = "年级"

    def __str__(self):
        return self.name


class Mission(models.Model):
    level = models.IntegerField("关卡", default=0)
    type_id = models.IntegerField("年级", choices=class_type)
    pub_time = models.DateTimeField("时间", default=timezone.now)

    class Meta:
        verbose_name = "关卡"
        verbose_name_plural = "关卡"

    def type(self):
        return self.get_type_id_display()

    def __str__(self):
        return str(self.level) + self.get_type_id_display()


class Ques(models.Model):
    title = models.TextField("题目")
    optA = models.CharField("A选项", max_length=100)
    optB = models.CharField("B选项", max_length=100)
    optC = models.CharField("C选项", max_length=100)
    optD = models.CharField("D选项", max_length=100)
    correct = models.CharField("答案", max_length=4, choices=(("1", "A"), ("2", "B"), ("3", "C"), ("4", "D")))
    type_id = models.IntegerField("年级", choices=class_type)
    level_id = models.ForeignKey(Mission)
    pub_time = models.DateTimeField("时间", default=timezone.now)

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = "题目"

    def correctOpt(self):
        return self.get_correct_display()

    def __str__(self):
        return self.title


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


# 结果
class Result(models.Model):
    point = models.IntegerField("分数", default=0)
    # openId = models.CharField("openId", max_length=150, blank=True, default="")
    type_id = models.IntegerField("年级", choices=class_type)
    level_id = models.IntegerField("关卡")
    # user_id = models.ForeignKey(UserInfo)
    user_id = models.ForeignKey(UserInfo, to_field="openId", blank=True, default="")
    time = models.CharField("时间", max_length=150, blank=True, default="")
    star = models.IntegerField("星星", default=0)

    class Meta:
        ordering = ["level_id"]
        verbose_name = "答题信息"
        verbose_name_plural = "答题信息"

    def __str__(self):
        return str(self.point)


# 总榜
class Total(models.Model):
    score = models.IntegerField("分数", default=0)
    type_id = models.IntegerField("年级", choices=class_type)
    user_id = models.ForeignKey(UserInfo, to_field="openId", blank=True, default="")

    class Meta:
        ordering = ["-score"]
        verbose_name = "总榜"
        verbose_name_plural = "总榜"

    def __str__(self):
        return str(self.score)

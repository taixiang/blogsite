from django.contrib import admin
from .models import Type, Blog, Me, Ascii, wordhtml, UserInfo, Shop, Food, FoodOrder, Category, Marry, JoinMsg
from django.db import models
from django import forms
from django.utils.safestring import mark_safe

# Register your models here.

admin.site.site_header = "后台管理"


class BlogAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'md_file')


class ImageWidget2(forms.FileInput):
    template = '%(input)s<br />%(image)s'

    def __init__(self, attrs=None, template=None, width=200, height=200):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget2, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        input_html = super(ImageWidget2, self).render(name, value, attrs)
        if hasattr(value, 'width') and hasattr(value, 'height'):

            image_html = '<img src="/upload/%s" width="100px" height="100px" />' % value.name

            output = self.template % {'input': input_html,
                                      'image': image_html}
        else:
            output = input_html
        return mark_safe(output)



class AsciiAdminqq(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('time','image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget2}}


class MarryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name',)
    list_filter = ('category_id',)  # 过滤器

class UserInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('nickName','openId')


class JoinMsgAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','phone','msg','remark','openId')
    list_filter =('msg',) #过滤器
    search_fields =('name', 'phone') #搜索字段

admin.site.register(Type)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Me)
admin.site.register(Ascii, AsciiAdminqq)
admin.site.register(wordhtml)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Shop)
admin.site.register(Food)
admin.site.register(FoodOrder)
admin.site.register(Category)
admin.site.register(Marry,MarryAdmin)
admin.site.register(JoinMsg,JoinMsgAdmin)
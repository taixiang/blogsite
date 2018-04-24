from django.contrib import admin
from .models import Type, Blog

# Register your models here.

admin.site.site_header = "后台管理"


class BlogAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'md_file')


admin.site.register(Type)
admin.site.register(Blog, BlogAdmin)

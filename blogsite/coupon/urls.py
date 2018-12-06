from django.conf.urls import url
from .views import index, type_list, detail, more_coupon, search, delete_excel, word_create, create_key, ques

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^more', more_coupon, name='more_coupon'),
    url(r'^price/(?P<type>.*)/$', type_list, name='type_list'),
    url(r'^detail/(?P<coupon_id>.*)/$', detail, name='detail'),
    url(r'^search', search, name='search'),
    url(r'^create_key', create_key, name='create_key'),
    url(r'^question', ques, name="ques"),
    # 根据excel 创建数据 删除文件
    url(r'^word_create_coupon', word_create, name='word_create'),
    # 删除过期数据
    url(r'^delete_tai_excel_xiang', delete_excel, name='delete_excel'),

]

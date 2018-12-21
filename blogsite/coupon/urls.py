from django.conf.urls import url
from .views import index, type_list, detail, more_coupon, search, delete_excel, word_create, create_key, ques, \
    post_advice, delete_all, good_list, like, goods_detail, favorites_list, favorite, get_wx_root, get_access_token

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^good_list', good_list, name='good_list'),
    url(r'^goods_detail', goods_detail, name='goods_detail'),
    url(r'^like', like, name='like'),
    url(r'^more', more_coupon, name='more_coupon'),
    url(r'^favorite/(?P<favorites_id>.*)/$', favorite, name='favorite'),
    url(r'^favorites_list/(?P<favorites_id>.*)/$', favorites_list, name='favorites_list'),
    url(r'^price/(?P<type>.*)/$', type_list, name='type_list'),
    url(r'^detail/(?P<coupon_id>.*)/$', detail, name='detail'),
    url(r'^search', search, name='search'),
    url(r'^create_key', create_key, name='create_key'),
    url(r'^question', ques, name="ques"),
    url(r'^post_advice', post_advice, name="post_advice"),
    # 根据excel 创建数据 删除文件
    url(r'^word_create_coupon', word_create, name='word_create'),
    # 删除过期数据
    url(r'^delete_tai_excel_xiang', delete_excel, name='delete_excel'),
    # 删除所有数据
    url(r'^delete_all', delete_all, name='delete_all'),
    url(r'^MP_verify_cFL29g0dxlethL6n.txt', get_wx_root, name='wx_root'),
    url(r'^get_access_token', get_access_token, name='get_access_token'),
]

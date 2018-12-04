from django.conf.urls import url
from .views import index, type_list, detail, more_coupon, search

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^more', more_coupon, name='more_coupon'),
    url(r'^price/(?P<type>.*)/$', type_list, name='type_list'),
    url(r'^detail/(?P<coupon_id>.*)/$', detail, name='detail'),
    url(r'^search', search, name='search')
]

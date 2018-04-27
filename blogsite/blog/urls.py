from django.conf.urls import url
from .views import index, detail, archive, category, category_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<blog_id>\d+)/detail/$', detail, name='detail'),
    url(r'^archive', archive, name='archive'),
    url(r'^category', category, name='category'),
    url(r'(?P<type_id>\d+)/category', category_detail, name='category_detail')

]

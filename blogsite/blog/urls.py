from django.conf.urls import url
from .views import index, detail, archive

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<blog_id>\d+)/detail/$', detail, name='detail'),
    url(r'^archive', archive, name='archive')
]

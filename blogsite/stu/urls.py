from django.conf.urls import url
from .views import index,moreImg,count
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^moreImg', moreImg, name='moreImg'),
    url(r'^count', count, name='count'),
]
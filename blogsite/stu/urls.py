from django.conf.urls import url
from .views import index,moreImg
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^moreImg', moreImg, name='moreImg'),
]
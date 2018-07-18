from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    # url(r'^getOpenId', views.getOpenId, name='getOpenId'),
    url(r'^postUserInfo', views.postUserInfo, name='postUserInfo'),
    url(r'^postResult', views.postResult, name='postResult'),
    url(r'^getOpenId', views.getOpenId, name='getOpenId'),
    url(r'^postPoint', views.postPoint, name='postPoint'),

]

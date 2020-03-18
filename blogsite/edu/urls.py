from django.conf.urls import url, handler404
from . import views

urlpatterns = [
    # url(r'^getOpenId', views.getOpenId, name='getOpenId'),
    url(r'^postUserInfo', views.postUserInfo, name='postUserInfo'),
    url(r'^postResult', views.postResult, name='postResult'),
    url(r'^getOpenId', views.getOpenId, name='getOpenId'),
    url(r'^getQQOpenId', views.getQQOpenId, name='getQQOpenId'),
    url(r'^postPoint', views.postPoint, name='postPoint'),
    url(r'^postError', views.postError, name='postError'),
    url(r'^postAdvice', views.postAdvice, name='postAdvice'),
    url(r'^postCopy', views.postCopy, name='postCopy'),
    url(r'^test', views.test, name='test'),

]

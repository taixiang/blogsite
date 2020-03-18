"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from django.conf import settings
import os
from django.conf.urls.static import static
from rest_framework import routers
from edu import views as edu_view
from blog import apis as blogApi

router = routers.DefaultRouter()
router.register(r'missions', edu_view.MissionViewSet, base_name='missions')
router.register(r'ques', edu_view.QuesViewSet, base_name='ques')
router.register(r'result', edu_view.ResultViewSet, base_name='result')
router.register(r'total', edu_view.TotalViewSet, base_name='total')
router.register(r'p_ques', edu_view.QuestionViewSet, base_name='p_ques')
router.register(r'm_ques', edu_view.QuestionMViewSet, base_name='m_ques')
router.register(r'rank', edu_view.RankViewSet, base_name='rank')
router.register(r'wrongQues', edu_view.WrongViewSet, base_name='wrongQues')
router.register(r'error', edu_view.ErrorViewSet, base_name='error')
router.register(r'sentence', edu_view.SentenceViewSet, base_name='sentence')
router.register(r'login', blogApi.LoginApi, base_name='login')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^$', views.index),
    url(r'^root.txt', views.get_root),
    url(r'^MP_verify_cFL29g0dxlethL6n.txt', views.get_wx_root),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^edu/', include('edu.urls', namespace='edu', app_name='edu')),
    url(r'^love/', include('love.urls', namespace="love", app_name="love")),
    url(r'^517518/', include('stu.urls', namespace='stu', app_name='stu')),
    url(r'^msmm/', include('msmm.urls', namespace="msmm", app_name="msmm")),
    url(r'^youhui/', include('coupon.urls', namespace="coupon", app_name="coupon")),

]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    urlpatterns += static('/upload/', document_root=media_root)

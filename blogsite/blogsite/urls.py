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

router = routers.DefaultRouter()
router.register(r'missions', edu_view.MissionViewSet, base_name='missions')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^$', views.index),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, 'upload/')
    urlpatterns += static('/upload/', document_root=media_root)
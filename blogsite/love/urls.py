from django.conf.urls import url
from .views import index ,marry

urlpatterns = [
    # url(r'^$', index, name='index'),
    url(r'^$', marry, name='marry'),
]

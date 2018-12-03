from django.conf.urls import url
from .views import index, type_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<type>.*)/$', type_list, name='type_list'),

]

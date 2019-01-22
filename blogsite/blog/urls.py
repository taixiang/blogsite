from django.conf.urls import url
from .views import index, detail, archive, category, category_detail, about, post_img,\
    get_root,category_name,validate_code,wordtohtml
from .apis import login

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<blog_id>\d+)/detail/$', detail, name='detail'),
    url(r'^archive', archive, name='archive'),
    url(r'^category', category, name='category'),
    url(r'(?P<type_id>\d+)/category', category_detail, name='category_detail'),
    url(r'^magic', category_name, name='category_name'),
    url(r'^about', about, name="about"),
    url(r'^post_img', post_img, name="post_img"),
    url(r'^validate',validate_code,name="validate"),
    url(r'^wordtohtml', wordtohtml, name="wordtohtml"),
    url(r'^login', login, name="login"),

]

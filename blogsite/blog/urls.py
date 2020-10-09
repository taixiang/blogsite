from django.conf.urls import url
from .views import index, detail, archive, category, category_detail, about, post_img, \
    get_root, category_name, validate_code, wordtohtml, talk, agent, marry
from .apis import login, analyze, blogs, blog_detail, foodList, getOpenId, postUserInfo, home_swiper, type_list, \
    get_img, getUserInfo, postJoinMsg, getJoinMsg, get_seat

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'(?P<blog_id>\d+)/detail/$', detail, name='detail'),
    url(r'^talk', talk, name='talk'),
    url(r'^archive', archive, name='archive'),
    url(r'^category', category, name='category'),
    url(r'(?P<type_id>\d+)/category', category_detail, name='category_detail'),
    url(r'^magic', category_name, name='category_name'),
    url(r'^about', about, name="about"),
    # url(r'^post_img', post_img, name="post_img"),
    url(r'^validate',validate_code,name="validate"),
    # url(r'^wordtohtml', wordtohtml, name="wordtohtml"),
    url(r'^login', login, name="login"),
    url(r'^home', analyze, name="home"),
    url(r'^blogs', blogs, name="blogs"),
    url(r'^blog_detail/(?P<blog_id>\d+)', blog_detail, name='blog_detail'),
    url(r'^foodList',foodList,name="foodList"),
    url(r'^getOpenId', getOpenId, name="getOpenId"),
    url(r'^postUserInfo', postUserInfo, name='postUserInfo'),
    url(r'^getUserInfo', getUserInfo, name='getUserInfo'),
    url(r'^agent', agent,name='agent'),
    url(r'^marry', marry,name='marry'),
    url(r'^wswiper', home_swiper, name='home_swiper'),
    url(r'^typeList', type_list, name='type_list'),
    url(r'^getImg', get_img, name='get_img'),
    url(r'^getSeat', get_seat, name='get_seat'),
    url(r'^postJoinMsg', postJoinMsg, name='postJoinMsg'),
    url(r'^getJoinMsg', getJoinMsg, name='getJoinMsg'),

]

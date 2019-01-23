from django.contrib import auth
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.decorators import api_view
import json


class LoginApi(viewsets.ViewSet):
    def list(self, request):
        return Response(OrderedDict([
            ('code', 200),
            ('msg', "登录成功"),
            ('results', "1111")
        ]))


def api_result(code, msg, data=None):
    return Response(OrderedDict([
        ('code', code),
        ('msg', msg),
        ("data", data)
    ]))


def get_decorator(default_value):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return default_value

        return new_func

    return decorator



@get_decorator("登录失败")
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        name = data['name']
        pwd = data['pwd']
        user = auth.authenticate(username=name, password=pwd)
        print(user)
        if user is not None:
            print(user.is_active)
            if user.is_active:
                auth.login(request, user)
            return api_result(200, "登录成功")
        else:
            return api_result(500, "登录失败")

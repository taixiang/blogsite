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
            ('results', "1111")
        ]))


@api_view(['POST'])
def login(request):
    try:
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
                return Response(OrderedDict([
                    ('code', 200),
                    ('msg', "登录成功")
                ]))
            else:
                return Response(OrderedDict([
                    ('code', 500),
                    ('msg', "登录失败")
                ]))
    except:
        return Response(OrderedDict([
            ('code', 500),
            ('msg', "登录失败")
        ]))

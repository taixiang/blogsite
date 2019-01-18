from django.contrib import auth
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict


class LoginApi(viewsets.ViewSet):
    def list(self, request):
        return Response(OrderedDict([
            ('code', 200),
            ('results', "1111")
        ]))

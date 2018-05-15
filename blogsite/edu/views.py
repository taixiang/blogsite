from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from .models import Mission, ClassType, Ques, UserInfo, Result
from .serializer import MissionSerializer, QuesSerializer, ResultSerializer
import json
import time
from django.http import JsonResponse, HttpResponse


# Create your views here.
# 关卡
class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def list(self, request, *args, **kwargs):
        type = request.GET.get('type')
        self.queryset = self.queryset.filter(type_id=type)
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('code', 200),
            ('results', serializer.data)
        ]))


# 题目
class QuesViewSet(viewsets.ModelViewSet):
    queryset = Ques.objects.all()
    serializer_class = QuesSerializer

    def list(self, request, *args, **kwargs):
        print("=========")
        type_id = request.GET.get('type_id')
        level_id = request.GET.get('level_id')

        self.queryset = Ques.objects.filter(type_id=type_id, level_id=level_id)
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('code', 500),
            ('results', serializer.data)
        ]))

    def retrieve(self, request, *args, **kwargs):
        pkid = kwargs.get("pk")
        data = Ques.objects.get(id=pkid)
        serializer = self.get_serializer(data)
        return Response(OrderedDict([
            ('code', 200),
            ('results', serializer.data)
        ]))


# 排行榜
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


# 用户信息保存
@csrf_exempt
def postUserInfo(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(data)
        data['time'] = t
        print(data['openId'])
        user = UserInfo.objects.update_or_create(openId=data['openId'], defaults=data)[0]
        user.save()
    return JsonResponse(None, safe=False)


# 结果信息
@csrf_exempt
def postResult(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(data)
        data['time'] = t

        result = Result(**data)
        result.save()

        res = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"
    return JsonResponse(res, safe=False)

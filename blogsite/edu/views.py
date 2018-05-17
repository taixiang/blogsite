from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from .models import Mission, ClassType, Ques, UserInfo, Result, Total
from .serializer import MissionSerializer, QuesSerializer, ResultSerializer, TotalSerializer
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
        print(serializer.data)
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
            ('code', 200),
            ('results', serializer.data)
        ]))


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request, *args, **kwargs):
        print("=========")
        type_id = request.GET.get('type_id')
        user_id = request.GET.get('user_id')
        m_count = Mission.objects.filter(type_id=type_id).count()
        m_count = 4

        self.queryset = Result.objects.filter(type_id=type_id, user_id=user_id)
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        data = list(serializer.data)

        # print(data[len(data) - 1])
        num = len(data)

        if num == 0:  # 一关未答
            print("11111111")
            data.append({"star": 0, "level_id": 1})
            for i in range(num + 2, m_count + 1):
                data.append({"star": -1, "level_id": i})
        elif data[num - 1]["star"] >= 2 and num < m_count:  # 最后一关是两颗星，则开启下一关
            print("222222222")
            data.append({"star": 0, "level_id": num + 1})
            if num + 1 < m_count:
                for i in range(num + 2, m_count + 1):
                    data.append({"star": -1, "level_id": i})
        elif num < m_count:  # 剩余未作答
            print("33333333333")
            for i in range(num + 1, m_count + 1):
                data.append({"star": -1, "level_id": i})

        return Response(OrderedDict([
            ('code', 200),
            ('results', data)
        ]))


# 排行榜(区别type)
class TotalViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer


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

        total = Total.objects.get_or_create(user_id_id=data["user_id_id"], type_id=data["type_id"])[0]
        total.score += data["point"]
        total.save()

        result = Result(**data)
        result.save()

        res = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"
    return JsonResponse(res, safe=False)

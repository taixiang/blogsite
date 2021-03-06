from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from .models import Mission, ClassType, Ques, UserInfo, Result, Total, Question, \
    Score, WrongQues, ErrorInfo, Advice, QuestionM, Sentence, SentenceUser
from .serializer import MissionSerializer, QuesSerializer, ResultSerializer, \
    TotalSerializer, QuestionSerializer, RankSerializer, WrongSerializer, ErrorSerializer, ResultPagination, \
    QuestionMSerializer, SentenceSerializer
import json
import time
from django.http import JsonResponse, HttpResponse
import random
import requests


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
        data = list(serializer.data)
        random.shuffle(data)
        return Response(OrderedDict([
            ('code', 200),
            ('results', data)
        ]))


# 用户关卡
class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request, *args, **kwargs):
        print("=========")
        type_id = request.GET.get('type_id')
        user_id = request.GET.get('user_id')
        m_count = Mission.objects.filter(type_id=type_id).count()
        # m_count = 4

        if m_count == 0:
            return Response(OrderedDict([
                ('code', 200),
                ('results', [])
            ]))

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


# 排行榜
class TotalViewSet(viewsets.ModelViewSet):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer

    def list(self, request, *args, **kwargs):
        print("=========")
        type_id = request.GET.get('type_id')

        self.queryset = Total.objects.filter(type_id=type_id)
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('code', 200),
            ('results', serializer.data)
        ]))


# 结果信息
@csrf_exempt
def postResult(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data['time'] = t

        # 同一班级、关卡，新分数大于原先的分数则保存
        result = Result.objects.get_or_create(user_id_id=data["user_id_id"], type_id=data["type_id"],
                                              level_id=data["level_id"])[0]
        print(data["point"])
        print(result.point)
        if data["point"] > result.point:
            print("============")
            curPoint = result.point
            result.point = data["point"]
            result.star = data["star"]
            result.time = data["time"]
            result.save()
            # 总分 先减去当前保存 再加上最新的分数
            total = Total.objects.get_or_create(user_id_id=data["user_id_id"], type_id=data["type_id"])[0]
            total.score -= curPoint
            total.score += data["point"]
            total.save()

        res = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"
    return JsonResponse(res, safe=False)


# ===================================================================================================================
# 获取openid
def getOpenId(request):
    jscode = request.GET.get('code')
    print(jscode)
    print(111111)
    resp = requests.get(
        "https://api.weixin.qq.com/sns/jscode2session?appid=wxf5e6ccf6b668dcd2&secret=b82a131139a2be2fdbfba95e4ed63d3e&js_code=" + str(
            jscode) + "&grant_type=authorization_code")
    print(resp.text)
    # data = serializers.serialize("json", resp.text)
    return HttpResponse(json.dumps(resp.text), content_type="application/json")


def getQQOpenId(request):
    jscode = request.GET.get('code')
    print(jscode)
    print(111111)
    resp = requests.get(
        "https://api.q.qq.com/sns/jscode2session?appid=1110240408&secret=ggDFVipPDnsXkbzz&js_code=" + str(
            jscode) + "&grant_type=authorization_code")
    print(resp.text)
    # data = serializers.serialize("json", resp.text)
    return HttpResponse(json.dumps(resp.text), content_type="application/json")


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


# 小学题目
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        try:
            # 随机获取10条
            queryset = Question.objects.order_by("?")[:10]
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 初中题目
class QuestionMViewSet(viewsets.ModelViewSet):
    queryset = QuestionM.objects.all()
    serializer_class = QuestionMSerializer

    def list(self, request, *args, **kwargs):
        try:
            # 随机获取10条
            queryset = QuestionM.objects.order_by("?")[:10]
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 上传结果
@csrf_exempt
def postPoint(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data["time"] = t
        # 答对提交
        score = Score.objects.get_or_create(user_id_id=data["user_id_id"], type_id=data["type_id"])[0]
        score.point += data["point"]
        score.time = data["time"]
        score.save()

        # 错题收集
        wrongs = data["wrongs"]
        if len(wrongs) > 0:
            print("========错题")
            print(wrongs)
            answers = data["answers"]
            wrong_list = wrongs.split(",")
            answer_list = answers.split(",")
            for i, w in enumerate(wrong_list):
                wq = WrongQues(user_id_id=data["user_id_id"], type_id=data["type_id"])
                wq.qId = wrong_list[i]
                wq.answer = answer_list[i]
                wq.time = data["time"]
                wq.save()

    res = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"
    return JsonResponse(res, safe=False)


# 纠错信息
@csrf_exempt
def postError(request):
    print("===================")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data["time"] = t

        ErrorInfo(**data).save()
        result = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"

    return JsonResponse(result, safe=False)


# 新排行榜
class RankViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Score.objects.all()
    serializer_class = RankSerializer

    def list(self, request, *args, **kwargs):
        try:
            print("=========")
            type_id = request.GET.get('type_id')

            self.queryset = Score.objects.filter(type_id=type_id).order_by("-point")
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 错题集
class WrongViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = WrongQues.objects.all()
    serializer_class = WrongSerializer

    def list(self, request, *args, **kwargs):
        try:
            type_id = request.GET.get('type_id')
            user_id_id = request.GET.get('user_id')
            self.queryset = WrongQues.objects.filter(user_id_id=user_id_id).filter(type_id=type_id)
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 纠错
class ErrorViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = ErrorInfo.objects.all()
    serializer_class = ErrorSerializer

    def list(self, request, *args, **kwargs):
        try:
            type_id = request.GET.get('type_id')
            user_id_id = request.GET.get('user_id')
            self.queryset = ErrorInfo.objects.filter(user_id_id=user_id_id).filter(type_id=type_id)
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))
            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


# 句子
class SentenceViewSet(viewsets.ModelViewSet):
    pagination_class = ResultPagination
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

    def list(self, request, *args, **kwargs):
        try:
            # 随机获取10条
            # queryset = Sentence.objects.order_by("?")[:10]
            queryset = self.filter_queryset(self.queryset)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return Response(OrderedDict([
                    ('code', 200),
                    ('count', self.paginator.page.paginator.count),
                    ('next', self.paginator.get_next_link()),
                    ('previous', self.paginator.get_previous_link()),
                    ('results', serializer.data)
                ]))

            serializer = self.get_serializer(queryset, many=True)
            return Response(OrderedDict([
                ('code', 200),
                ('results', serializer.data)
            ]))
        except:
            return Response(OrderedDict([
                ('code', 500),
                ('results', None)
            ]))


@csrf_exempt
def postAdvice(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data["time"] = t

        Advice(**data).save()
        result = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"

    return JsonResponse(result, safe=False)


# 复制提交
@csrf_exempt
def postCopy(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data["time"] = t

        SentenceUser(**data).save()
        result = "{ \"code\":" + "200" + ",\"result\":" + "\"提交成功\"}"

    return JsonResponse(result, safe=False)


def test(request):
    return render(request, "test.html")

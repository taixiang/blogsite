from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from .models import Mission, ClassType, Ques
from .serializer import MissionSerializer, QuesSerializer


# Create your views here.
# 关卡
class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def list(self, request, *args, **kwargs):
        type = request.GET.get('type')
        if type == 1:
            ot = ClassType.objects.get(name="小学")
        else:
            ot = ClassType.objects.get(name="初中")
        self.queryset = self.queryset.filter(type_id=ot.id)
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('code', 200),
            ('results', serializer.data)
        ]))


class QuesViewSet(viewsets.ModelViewSet):
    queryset = Ques.objects.all()
    serializer_class = QuesSerializer

    def list(self, request, *args, **kwargs):
        return Response(OrderedDict([
            ('code', 500),
            ('results', None)
        ]))

    def retrieve(self, request, *args, **kwargs):
        pkid = kwargs.get("pk")
        data = Ques.objects.get(id=pkid)
        serializer = self.get_serializer(data)
        return Response(OrderedDict([
            ('code', 200),
            ('results', serializer.data)
        ]))

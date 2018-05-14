from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from collections import OrderedDict
from .models import Mission, ClassType
from .serializer import MissionSerializer


# Create your views here.
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

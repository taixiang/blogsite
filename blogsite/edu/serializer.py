from rest_framework import serializers
from .models import Mission, ClassType, Ques, UserInfo, Result, Total


class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('nickName', 'openId')


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'level', 'type')


class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ques
        fields = ("title", 'optA', 'optB', 'optC', 'optD', 'correctOpt')


class ResultSerializer(serializers.ModelSerializer):
    # user_id = SubCateSerializer(many=False)

    class Meta:
        model = Result
        fields = ("point", 'level_id', 'star')


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ("score", "type_id")

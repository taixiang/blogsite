from rest_framework import serializers
from .models import Mission, ClassType, Ques, UserInfo, Result


class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('nickName',)


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('level', 'type')


class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ques
        fields = ("title", 'optA', 'optB', 'optC', 'optD', 'correctOpt')


class ResultSerializer(serializers.ModelSerializer):
    # openId = SubCateSerializer(many=False)
    nickName = serializers.SerializerMethodField("get_name")

    class Meta:
        model = Result
        fields = ("point", 'nickName')

    def get_name(self, obj):
        return UserInfo.objects.get(openId=obj.openId).nickName

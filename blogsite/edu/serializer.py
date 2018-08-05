from rest_framework import serializers
from .models import Mission, ClassType, Ques, UserInfo, Result, Total, Question, Score, WrongQues, QuestionM, ErrorInfo
from django.forms.models import model_to_dict


class SubCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('nickName', 'openId', 'avatarUrl')


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
    user_id = SubCateSerializer(many=False)

    class Meta:
        model = Total
        fields = ("score", "type_id", "user_id")


# 小学题目
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "title", "optA", "optB", "optC", "optD", "correct")


# 排行榜
class RankSerializer(serializers.ModelSerializer):
    user_id = SubCateSerializer(many=False)

    class Meta:
        model = Score
        fields = ("point", "type_id", "user_id")


# 错题集
class WrongSerializer(serializers.ModelSerializer):
    pId = serializers.SerializerMethodField("getQues")

    class Meta:
        model = WrongQues
        fields = ("id","answer", "pId")

    def getQues(self, obj):
        if obj.type_id == 1:
            queryset = Question.objects.get(id=obj.qId)
        else:
            queryset = QuestionM.objects.get(id=obj.qId)
        content = model_to_dict(queryset)
        return content


# 纠错
class ErrorSerializer(serializers.ModelSerializer):
    pId = serializers.SerializerMethodField("getQues")

    class Meta:
        model = ErrorInfo
        fields = ("id","content", "pId")

    def getQues(self, obj):
        if obj.type_id == 1:
            queryset = Question.objects.get(id=obj.qId)
        else:
            queryset = QuestionM.objects.get(id=obj.qId)
        content = model_to_dict(queryset)
        return content

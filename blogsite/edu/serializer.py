from rest_framework import serializers
from .models import Mission, ClassType, Ques


class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ('name',)


class MissionSerializer(serializers.ModelSerializer):
    # type_id = SubTypeSerializer()

    class Meta:
        model = Mission
        fields = ('level',)


class QuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ques
        fields = ("title",)

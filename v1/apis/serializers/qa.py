from rest_framework import serializers

from v1.models import QAGroup, QAItem
from v1.models import Place


class QAGroupListAPIQuerySerializer(serializers.Serializer):
    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), required=True
    )


class QAGroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QAGroup
        fields = ("id", "name", "description")


class QAItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QAItem
        fields = ("id", "question", "answer", "group", "place")

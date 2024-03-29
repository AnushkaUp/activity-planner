from rest_framework import serializers

from v1.models import Event


class EventModelSerializer(serializers.ModelSerializer):
    staus = serializers.SerializerMethodField()

    class Meta:
        model = Event
        exclude = (
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
            "is_active",
            "udf_1",
            "udf_2",
            "udf_3",
        )

    def get_status(self, obj):
        return obj.status

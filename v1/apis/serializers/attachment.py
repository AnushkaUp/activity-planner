from rest_framework import serializers

from v1.models import Attachment, AttachmentGroup
from v1.models.place import Place


class AttachmentGroupListAPIQuerySerializer(serializers.Serializer):
    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), required=True
    )


class AttachmentGroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachmentGroup
        fields = ("id", "name")


class AttachmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
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

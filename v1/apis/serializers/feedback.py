from rest_framework import serializers

from v1.apis.serializers.user import UserSerializer
from v1.models import Feedback, Place


class FeedbackListAPIQuerySerializer(serializers.Serializer):
    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), required=False
    )
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Feedback.objects.all(), required=False
    )

    def validate(self, attrs):
        if not attrs.get("parent") and not attrs.get("place"):
            raise serializers.ValidationError(
                {"parent": "Either parent or place is required."}
            )
        return super().validate(attrs)


class FeedbackModelSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Feedback.objects.all(), required=False
    )
    place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(), required=False
    )
    created_by_name = serializers.CharField(
        source="created_by.username", read_only=True
    )
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "comment",
            "rating",
            "parent",
            "place",
            "edited",
            "owner",
            "created_by_name",
            "owner",
            "created_at",
        ]

    def validate(self, attrs):
        if not attrs.get("parent") and not attrs.get("place"):
            raise serializers.ValidationError(
                {"parent": "Either parent or place is required."}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        instance = (
            Feedback.objects.filter_active(
                place=validated_data.get("place"),
                owner=self.context["request"].user,
            )
            | Feedback.objects.filter_active(
                parent=validated_data.get("parent"),
                owner=self.context["request"].user,
            )
        ).first()
        if instance:
            return self.update(instance, validated_data)
        validated_data["owner"] = self.context["request"].user
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user
        validated_data["edited"] = True
        return super().update(instance, validated_data)

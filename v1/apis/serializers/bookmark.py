from v1.models import Bookmark, Place
from django.contrib.auth import get_user_model
from .place import PlaceModelSerializer
from rest_framework import serializers

User = get_user_model()


class BookmarkModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter())
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.filter())
    is_active = serializers.BooleanField(required=False)

    class Meta:
        model = Bookmark
        exclude = (
            "udf_1",
            "udf_2",
            "udf_3",
        )
        read_only_fields = ["user", "place", "is_active"]
        # depth = 1

    def create(self, validated_data):
        existing_bookmark = Bookmark.objects.filter(
            place=validated_data.get("place"),
            user=validated_data.get("user")
        ).order_by("-created_at").first()
        if existing_bookmark:
            existing_bookmark.is_active = not existing_bookmark.is_active
            return super().update(existing_bookmark, validated_data)
        validated_data["created_by"] = self.context["request"].user
        validated_data["updated_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["place"] = PlaceModelSerializer(instance.place).data
        return data

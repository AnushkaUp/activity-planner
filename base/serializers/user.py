from rest_framework import serializers
from django.contrib.auth import get_user_model

from v1.constants import AttachmentTypeChoices

User = get_user_model()


class UserBasicModelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
            "images",
        ]
        read_only_fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
        ]
        depth = 1

    def get_images(self, obj):
        images = obj.profile_pics.filter_active(file_type=AttachmentTypeChoices.IMAGE)
        if images.exists():
            return [
                {
                    "name": image.name,
                    "mime_type": image.mime_type,
                    "url": image.file.url,
                }
                for image in images
            ]
        return None

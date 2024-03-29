from rest_framework import serializers
from django.contrib.auth import get_user_model

from v1.constants import AttachmentTypeChoices


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    employer = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "employer",
            "groups",
            "profile",
            "images",
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

    def get_employer(self, obj):
        if obj.profile.employer:
            return {"id": obj.profile.employer.id, "name": obj.profile.employer.name}
        return None

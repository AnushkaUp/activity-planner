from rest_framework import serializers
from django.db import models
from base.constants.profile import ProfileRoleChoices
from base.serializers.state import StateModelSerializer
from v1.apis.serializers.feedback import FeedbackModelSerializer
from v1.apis.serializers.user import UserSerializer
from v1.constants import AttachmentTypeChoices

from v1.models import (
    Place,
    GroupType,
    AreaType,
    TransPortType,
    Atmosphere,
    Activity,
    ActivityCategory,
    SpacingType,
    Address,
    Menu,
)


class GroupTypeModelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = GroupType
        fields = ["id", "name", "images"]

    def get_images(self, obj):
        images = obj.icons.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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


class AreaTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaType
        fields = ["id", "name"]


class TransPortTypeModelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = TransPortType
        fields = ["id", "name", "images", "description"]

    def get_images(self, obj):
        images = obj.icons.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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


class AtmosphereModelSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Atmosphere
        fields = ["id", "name", "images"]

    def get_images(self, obj):
        images = obj.icons.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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


class ActivityCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ["id", "name"]


class ActivityModelSerializer(serializers.ModelSerializer):
    category = ActivityCategoryModelSerializer()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ["id", "name", "category", "images"]

    def get_images(self, obj):
        images = obj.icons.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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


class SpacingTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpacingType
        fields = ["id", "name"]


class AddressModelSerializer(serializers.ModelSerializer):
    state = StateModelSerializer()

    class Meta:
        model = Address
        exclude = [
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "is_active",
            "udf_1",
            "udf_2",
            "udf_3",
        ]


class MenuModelSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    images = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["id", "name", "description", "price", "category", "images"]

    def get_images(self, obj):
        images = obj.attachments.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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


class PlaceModelSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    group_type = GroupTypeModelSerializer(many=True)
    area_type = AreaTypeModelSerializer(many=True)
    available_transport = TransPortTypeModelSerializer(many=True)
    atmosphere = AtmosphereModelSerializer(many=True)
    activity = ActivityModelSerializer(many=True)
    spacing = SpacingTypeModelSerializer()
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    address = AddressModelSerializer(source="addresses", many=True)
    rating_count = serializers.SerializerMethodField()
    rating_average = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Place
        # fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "is_active",
        ]
        depth = 0
        exclude = (
            "udf_1",
            "udf_2",
            "udf_3",
        )

    def get_images(self, obj):
        images = obj.attachment_set.filter_active(file_type=AttachmentTypeChoices.IMAGE)
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

    def get_videos(self, obj):
        videos = obj.attachment_set.filter_active(file_type=AttachmentTypeChoices.VIDEO)
        if videos.exists():
            return [
                {
                    "name": video.name,
                    "mime_type": video.mime_type,
                    "url": video.file.url,
                }
                for video in videos
            ]
        return None

    def get_rating_count(self, obj):
        return obj.feedback_set.filter_active(parent__isnull=True, rating__gt=0).count()

    def get_rating_average(self, obj):
        return round(
            (
                obj.feedback_set.filter_active(
                    parent__isnull=True, rating__gt=0
                ).aggregate(models.Avg("rating"))["rating__avg"]
                or 0.0
            ),
            2,
        )

    def get_is_bookmarked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.bookmarks.filter_active(user=request.user).exists()
        return False


class PlaceDetailModelSerializer(PlaceModelSerializer):
    review = serializers.SerializerMethodField()
    staff_review = serializers.SerializerMethodField()
    place_staff_review = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    reviews_rating_count = serializers.SerializerMethodField()
    menus = MenuModelSerializer(source="menu", many=True)

    def get_review(self, obj):
        reviews = obj.feedback_set.filter_active(
            parent__isnull=True, rating__gt=0
        ).order_by("-created_at")
        if reviews.exists():
            review = reviews.first()
            return FeedbackModelSerializer(review).data
        return None

    def get_staff_review(self, obj):
        reviews = obj.feedback_set.filter_active(
            parent__isnull=True,
            rating__gt=0,
            created_by__profile__role=ProfileRoleChoices.STAFF,
        ).order_by("-created_at")
        if reviews.exists():
            review = reviews.first()
            return FeedbackModelSerializer(review).data
        return None

    def get_place_staff_review(self, obj):
        reviews = obj.feedback_set.filter_active(
            parent__isnull=True,
            rating__gt=0,
            created_by__profile__role=ProfileRoleChoices.PLACE_STAFF,
        ).order_by("-created_at")
        if reviews.exists():
            review = reviews.first()
            return FeedbackModelSerializer(review).data
        return None

    def get_reviews_count(self, obj):
        return obj.feedback_set.filter_active(parent__isnull=True, rating__gt=0).count()

    def get_reviews_rating_count(self, obj):
        final_map = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
        }
        for item in (
            obj.feedback_set.filter_active(parent__isnull=True, rating__gt=0)
            .values("rating")
            .annotate(count=models.Count("*"))
            .order_by("rating")
            .values("rating", "count")
        ):
            final_map[item["rating"]] = round(
                item["count"] / self.get_reviews_count(obj), 2
            )
        return final_map

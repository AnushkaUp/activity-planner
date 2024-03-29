from rest_framework import serializers
from rest_framework.fields import empty

from v1.models import ActivityPlan, ActivityPlanItem


class ActivityPlanItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPlanItem
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

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        validated_data["updated_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user
        return super().update(instance, validated_data)


class ActivityPlanModelSerializer(serializers.ModelSerializer):
    lines = ActivityPlanItemModelSerializer(many=True)

    def __init__(self, instance=None, data=..., **kwargs):
        self.is_many = True if kwargs.get("many") else False
        super().__init__(instance, data, **kwargs)

    class Meta:
        model = ActivityPlan
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

    def to_representation(self, instance):
        if self.is_many:
            self.fields.pop("lines")
        return super().to_representation(instance)

    def create(self, validated_data):
        validated_data["plan_of"] = self.context["request"].user
        validated_data["created_by"] = self.context["request"].user
        validated_data["updated_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.context["request"].user
        return super().update(instance, validated_data)

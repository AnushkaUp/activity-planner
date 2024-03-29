from rest_framework import serializers

from base.models import State


class StateModelSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(source="country.name")

    class Meta:
        model = State
        fields = ["id", "name", "country"]

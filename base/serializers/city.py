from rest_framework import serializers

from base.models import City


class CityModelSerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField(source="state.name")
    country = serializers.StringRelatedField(source="state.country.name")

    class Meta:
        model = City
        fields = ["id", "name", "state", "country"]

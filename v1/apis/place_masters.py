from rest_framework.generics import ListAPIView, RetrieveAPIView
from base.models import City
from base.serializers.city import CityModelSerializer

from v1.models import (
    AreaType,
    GroupType,
    TransPortType,
    Atmosphere,
    ActivityCategory,
    SpacingType,
)
from v1.apis.serializers import (
    GroupTypeModelSerializer,
    AreaTypeModelSerializer,
    ActivityCategoryModelSerializer,
    SpacingTypeModelSerializer,
    AtmosphereModelSerializer,
    TransPortTypeModelSerializer,
)


class GroupTypeListAPIView(ListAPIView):
    queryset = GroupType.objects.filter_active()
    serializer_class = GroupTypeModelSerializer


class AreaTypeListAPIView(ListAPIView):
    queryset = AreaType.objects.filter_active()
    serializer_class = AreaTypeModelSerializer


class ActivityCategoryListAPIView(ListAPIView):
    queryset = ActivityCategory.objects.filter_active()
    serializer_class = ActivityCategoryModelSerializer


class AtmosphereListAPIView(ListAPIView):
    queryset = Atmosphere.objects.filter_active()
    serializer_class = AtmosphereModelSerializer


class SpacingTypeListAPIView(ListAPIView):
    queryset = SpacingType.objects.filter_active()
    serializer_class = SpacingTypeModelSerializer


class TransportTypeListAPIView(ListAPIView):
    queryset = TransPortType.objects.filter_active()
    serializer_class = TransPortTypeModelSerializer


class CityListAPIView(ListAPIView):
    queryset = City.objects.filter_active()
    serializer_class = CityModelSerializer
    search_fields = ("name", "state__name", "state__country__name")

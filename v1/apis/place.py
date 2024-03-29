from rest_framework.generics import ListAPIView, RetrieveAPIView

from v1.models import Place, Activity
from v1.apis.serializers import (
    PlaceModelSerializer,
    ActivityModelSerializer,
    PlaceDetailModelSerializer,
)


class PlaceListAPIView(ListAPIView):
    permission_classes = []
    queryset = Place.objects.filter_active()
    serializer_class = PlaceModelSerializer
    filterset_fields = [
        "group_type",
        "area_type",
        "available_transport",
        "atmosphere",
        "activity",
        "activity__name",
        "activity__category__name",
        "addresses__city",
    ]
    search_fields = [
        "name",
        "activity__name",
        "activity__category__name",
        "addresses__city",
        "addresses__state__name",
    ]


class PlaceRetrieveAPIView(RetrieveAPIView):
    queryset = Place.objects.filter_active()
    serializer_class = PlaceDetailModelSerializer


class ActivityListAPIView(ListAPIView):
    permission_classes = []
    queryset = Activity.objects.filter_active()
    serializer_class = ActivityModelSerializer

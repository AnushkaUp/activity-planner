from rest_framework import generics
from django.utils import timezone

from v1.models import Event
from v1.apis.serializers import (
    EventModelSerializer,
)


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter_active()
    serializer_class = EventModelSerializer
    ordering = ["-created_at"]
    search_fields = [
        "title",
        "description",
        "addresses__city",
        "addresses__state__name",
    ]

    def get_queryset(self):
        return self.queryset.filter(end_date__gte=timezone.now())

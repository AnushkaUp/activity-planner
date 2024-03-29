from rest_framework import generics

from v1.apis.serializers import (
    QAGroupModelSerializer,
    QAItemModelSerializer,
    QAGroupListAPIQuerySerializer,
)
from v1.models import QAGroup, QAItem


class QAGroupListAPIView(generics.ListAPIView):
    queryset = QAGroup.objects.filter_active()
    serializer_class = QAGroupModelSerializer

    def get_queryset(self):
        query_serializer = QAGroupListAPIQuerySerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        query_params = query_serializer.validated_data
        return (
            QAGroup.objects.filter_active()
            .filter(items__place=query_params.get("place"))
            .distinct()
        )


class QAItemListAPIView(generics.ListAPIView):
    queryset = QAItem.objects.filter_active()
    serializer_class = QAItemModelSerializer
    filterset_fields = ("group", "place")

    def get_queryset(self):
        if not self.request.query_params.get("place"):
            return QAItem.objects.none()
        return super().get_queryset()

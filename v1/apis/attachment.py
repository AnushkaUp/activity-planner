from rest_framework import generics

from v1.apis.serializers import (
    AttachmentGroupModelSerializer,
    AttachmentModelSerializer,
    AttachmentGroupListAPIQuerySerializer,
)
from v1.models import Attachment, AttachmentGroup


class AttachmentGroupListAPIView(generics.ListAPIView):
    queryset = AttachmentGroup.objects.filter_active()
    serializer_class = AttachmentGroupModelSerializer

    def get_queryset(self):
        query_serializer = AttachmentGroupListAPIQuerySerializer(
            data=self.request.query_params
        )
        query_serializer.is_valid(raise_exception=True)
        query_params = query_serializer.validated_data
        return (
            AttachmentGroup.objects.filter_active()
            .filter(attachments__place=query_params.get("place"))
            .distinct()
        )


class AttachmentListAPIView(generics.ListAPIView):
    queryset = Attachment.objects.filter_active()
    serializer_class = AttachmentModelSerializer
    filterset_fields = ("group", "place", "file_type")

    def get_queryset(self):
        if not self.request.query_params.get("place"):
            return Attachment.objects.none()
        return super().get_queryset()

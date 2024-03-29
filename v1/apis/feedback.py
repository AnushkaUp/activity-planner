from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from v1.models import Feedback
from v1.apis.serializers import FeedbackModelSerializer, FeedbackListAPIQuerySerializer


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.filter_active()
    serializer_class = FeedbackModelSerializer
    ordering = ["-created_at"]
    search_fields = ["comment", "place__name", "owner__first_name", "owner__last_name"]

    def get_queryset(self):
        if self.request.method == "POST":
            return super().get_queryset()
        query_serializer = FeedbackListAPIQuerySerializer(
            data=self.request.query_params
        )
        query_serializer.is_valid(raise_exception=True)
        if query_serializer.validated_data.get("parent"):
            return Feedback.objects.filter_active(
                parent=query_serializer.validated_data["parent"]
            )
        return (
            super()
            .get_queryset()
            .filter(place=query_serializer.validated_data["place"])
        )


class FeedbackRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Feedback.objects.filter_active()
    serializer_class = FeedbackModelSerializer

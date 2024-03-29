from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from v1.models import ActivityPlan
from v1.apis.serializers import ActivityPlanModelSerializer


class ActivityPlanListCreateAPIView(ListCreateAPIView):
    queryset = ActivityPlan.objects.filter_active()
    serializer_class = ActivityPlanModelSerializer
    ordering = ["-created_at"]
    search_fields = ["name", "plan_of__first_name", "plan_of__last_name"]

    def get_queryset(self):
        return super().get_queryset().filter(plan_of=self.request.user)


class ActivityPlanRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ActivityPlan.objects.filter_active()
    serializer_class = ActivityPlanModelSerializer

    def get_queryset(self):
        return super().get_queryset().filter(plan_of=self.request.user)

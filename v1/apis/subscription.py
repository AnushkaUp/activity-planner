from rest_framework import generics

from v1.models import NewsLetterSubscription
from v1.apis.serializers import NewsLetterSubscriptionSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    queryset = NewsLetterSubscription.objects.filter_active()
    serializer_class = NewsLetterSubscriptionSerializer

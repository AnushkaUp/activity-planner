from v1.models import NewsLetterSubscription


from rest_framework import serializers


class NewsLetterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterSubscription
        fields = ("email",)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if NewsLetterSubscription.objects.filter(email=attrs.get("email")).exists():
            raise serializers.ValidationError(
                {"email": ["This email is already subscribed."]}
            )
        return attrs

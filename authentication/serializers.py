from typing import Any, Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework import serializers


User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.get_email_field_name()

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        user = User.objects.filter(email=attrs[self.username_field]).first()
        if not user:
            raise serializers.ValidationError(
                {"email": "Email address does not exists."}
            )
        if not user.is_active:
            raise serializers.ValidationError({"email": "Email address is not active."})
        if not user.check_password(attrs["password"]):
            raise serializers.ValidationError({"password": "Password is not correct."})

        data = {}
        refresh = self.get_token(user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data

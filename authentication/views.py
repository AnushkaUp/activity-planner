from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Country

from base.models.profile import Profile

# Create your views here.

GENDER_CHOICES = ["male", "female", "other"]
User = get_user_model()


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = serializers.DateField()
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    full_nane = serializers.CharField(max_length=60, read_only=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    def validate(self, data):
        if not data.get("first_name") and not data.get("last_name"):
            raise serializers.ValidationError(
                {"full_name": "Either first name or last name is required."}
            )
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError(
                {"email": "Email address already exists."}
            )
        return data

    def create(self, validated_data):
        username = validated_data["email"].split("@")[0]
        user = User.objects.create(
            username=username,
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            password=validated_data["password"],
        )
        profile = Profile.objects.create(
            user=user,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            country=validated_data.get("country"),
            gender=validated_data.get("gender"),
            date_of_birth=validated_data.get("date_of_birth"),
        )
        return user


class SignUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

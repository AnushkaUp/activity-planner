from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpView


urlpatterns = [
    path("token-obtain/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

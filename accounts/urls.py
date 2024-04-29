from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", UserRegistrationView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('<str:username>/', UserDetailView.as_view(), name='user_detail'),
]

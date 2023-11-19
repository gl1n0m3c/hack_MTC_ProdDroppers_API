from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView


urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
]

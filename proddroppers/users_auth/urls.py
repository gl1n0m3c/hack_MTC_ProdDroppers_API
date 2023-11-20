from django.urls import path

from users_auth.views import (
    ChangePasswordView,
    LoginUserAPIView,
    RegisterUserAPIView,
)

urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    path("login", LoginUserAPIView.as_view()),
    path("changepassword", ChangePasswordView.as_view()),
]

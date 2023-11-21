from django.urls import path

from users_auth.views import (
    ChangeEmailAPIView,
    ChangeFirstNameAndLastNameAPIView,
    ChangePasswordView,
    LoginUserAPIView,
    RegisterUserAPIView,
)

urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    path("login", LoginUserAPIView.as_view()),
    path("changepassword", ChangePasswordView.as_view()),
    path("changeemail", ChangeEmailAPIView.as_view()),
    path("changenames", ChangeFirstNameAndLastNameAPIView.as_view()),
]

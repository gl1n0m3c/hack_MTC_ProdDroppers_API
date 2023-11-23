from django.urls import path

from users_auth.views import (
    ChangePasswordView,
    ChangeUsernameAndEmail,
    LoginUserAPIView,
    RegisterUserAPIView,
)


app_name = "users_auth"

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view()),
    path("login/", LoginUserAPIView.as_view()),
    path("changepassword/", ChangePasswordView.as_view()),
    path("changedata/", ChangeUsernameAndEmail.as_view()),
]

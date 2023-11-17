from django.urls import path

from users_auth.views import (
    ChangePasswordPage, ChangeUserDataPage,
    LoginPage, logout_user, SignUpPage)

urlpatterns = [
    path("logout/", logout_user, name="logout"),
    path("signup/", SignUpPage.as_view(), name="signup"),
    path("login/", LoginPage.as_view(), name="login"),
    path("edituserdata/", ChangeUserDataPage.as_view(), name="editData"),
    path(
        "changepassword/", ChangePasswordPage.as_view(),
        name="changePassword"),
]

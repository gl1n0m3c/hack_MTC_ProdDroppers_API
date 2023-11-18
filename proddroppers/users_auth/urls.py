from django.urls import path

from users_auth.views import sign_up, logout, login, Test

urlpatterns = [
    path(
        "",
        Test.as_view(),
        name="test",
    ),
    path(
        "logout/",
        logout,
        name="logout",
    ),
    path(
        "signup/",
        sign_up,
        name="signup",
    ),
    path(
        "login/",
        login,
        name="login",
    ),
]

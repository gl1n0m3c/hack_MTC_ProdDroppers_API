from django.urls import path

from users.views import (
    DetailAPI,
    UsersAPI,
    UsersChangeImageAPI,
)


app_name = "users"

urlpatterns = [
    path(
        "",
        UsersAPI.as_view(),
        name="users",
    ),
    path(
        "profile/<int:pk>/",
        DetailAPI.as_view(),
        name="profile",
    ),
    path(
        "change_image/",
        UsersChangeImageAPI.as_view(),
        name="change_image",
    ),
]

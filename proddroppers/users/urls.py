from django.urls import path

from users.views import DetailAPI, UsersAPI, UsersChangeImageAPI


urlpatterns = [
    path(
        "",
        UsersAPI.as_view(),
    ),
    path(
        "profile/<int:pk>/",
        DetailAPI.as_view(),
    ),
    path(
        "change_image/",
        UsersChangeImageAPI.as_view(),
    ),
]

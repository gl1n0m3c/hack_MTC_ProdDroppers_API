from django.urls import path

from users.views import UserDetailAPI, UserFriendsAPI, UserFriendsWaitingAPI


urlpatterns = [
    path(
        "get_details/<int:pk>/",
        UserDetailAPI.as_view(),
    ),
    path(
        "friends/<int:pk>/",
        UserFriendsAPI.as_view(),
    ),
    path(
        "friends_waiting/<int:pk>/",
        UserFriendsWaitingAPI.as_view(),
    ),
]

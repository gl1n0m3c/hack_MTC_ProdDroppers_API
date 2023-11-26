from django.urls import path

from friends.views import (
    FriendsAddAPI,
    FriendsAPI,
    FriendsAsseptAPI,
    FriendsDeleteAPI,
    FriendsRejectAPI,
    FriendsWaitingAPI,
)


app_name = "friends"

urlpatterns = [
    path(
        "users_friends/<int:pk>/",
        FriendsAPI.as_view(),
        name="list",
    ),
    path(
        "users_waiting_friends/<int:pk>/",
        FriendsWaitingAPI.as_view(),
        name="waiting",
    ),
    path(
        "add/",
        FriendsAddAPI.as_view(),
        name="add",
    ),
    path(
        "assept/",
        FriendsAsseptAPI.as_view(),
        name="assept",
    ),
    path(
        "reject/",
        FriendsRejectAPI.as_view(),
        name="reject",
    ),
    path(
        "delete/",
        FriendsDeleteAPI.as_view(),
        name="delete",
    ),
]

from django.urls import path

from friends.views import (
    FriendsAddAPI,
    FriendsAPI,
    FriendsAsseptAPI,
    FriendsDeleteAPI,
    FriendsRejectAPI,
    FriendsWaitingAPI,
)


urlpatterns = [
    path(
        "list/<int:pk>/",
        FriendsAPI.as_view(),
    ),
    path(
        "waiting/<int:pk>/",
        FriendsWaitingAPI.as_view(),
    ),
    path(
        "add/",
        FriendsAddAPI.as_view(),
    ),
    path(
        "assept/",
        FriendsAsseptAPI.as_view(),
    ),
    path(
        "reject/",
        FriendsRejectAPI.as_view(),
    ),
    path(
        "delete/",
        FriendsDeleteAPI.as_view(),
    ),
]

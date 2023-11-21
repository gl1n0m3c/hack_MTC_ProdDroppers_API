from django.urls import path

from friends.views import FriendsAddAPI, FriendsAPI, FriendsWaitingAPI


urlpatterns = [
    path(
        "friends_list/<int:pk>/",
        FriendsAPI.as_view(),
    ),
    path(
        "friends_waiting/<int:pk>/",
        FriendsWaitingAPI.as_view(),
    ),
    path(
        "friends_add/",
        FriendsAddAPI.as_view(),
    ),
]

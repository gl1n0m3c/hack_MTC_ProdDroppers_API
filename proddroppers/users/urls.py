from django.urls import path

from users.views import DetailAPI, FriendsAddAPI, FriendsAPI, FriendsWaitingAPI


urlpatterns = [
    path(
        "profile/<int:pk>/",
        DetailAPI.as_view(),
    ),
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

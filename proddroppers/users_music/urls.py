from django.urls import path

from users_music.views import MusicAPI, MusicListAPI


app_name = "music"

urlpatterns = [
    path(
        "",
        MusicListAPI.as_view(),
        name="music_list",
    ),
    path(
        "<int:pk>/",
        MusicAPI.as_view(),
        name="music",
    ),
]

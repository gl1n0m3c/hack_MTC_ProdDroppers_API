from django.urls import path
from rooms.views import RoomsAPI
from rooms.views import chat_page


urlpatterns = [
    path("", RoomsAPI.as_view(), name="rooms"),
    path("create/", RoomsAPI.as_view(), name="rooms_create"),
    path("<int:room_id>/", chat_page, name="chat-page"),
]

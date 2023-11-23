from django.urls import path
from rooms.consumers import ChatRoomConsumer

websocket_urlpatterns = [
    path("<int:room_name>/", ChatRoomConsumer.as_asgi()),
]

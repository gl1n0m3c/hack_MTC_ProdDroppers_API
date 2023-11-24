from django.urls import path
from rooms.consumers import ChatRoomConsumer

websocket_urlpatterns = [
    path("<int:room_name>/<int:user_id>/", ChatRoomConsumer.as_asgi()),
]

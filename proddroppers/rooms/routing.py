from django.urls import path
from rooms.consumers import ChatRoomConsumer

websocket_urlpatterns = [
    path("<int:room_id>/<int:user_id>/", ChatRoomConsumer.as_asgi()),
]

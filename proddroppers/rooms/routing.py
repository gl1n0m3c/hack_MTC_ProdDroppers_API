from django.urls import path, include
from rooms.consumers import ChatRoomConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("<int:room_name>/", ChatRoomConsumer.as_asgi()),
]

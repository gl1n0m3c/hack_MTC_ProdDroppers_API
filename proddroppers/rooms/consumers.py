import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rooms.models import (
    Rooms,
    Messages,
)
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_id = text_data_json["user_id"]
        username = await self.get_user(user_id)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chatroom_message",
                "message": message,
                "username": username,
            },
        )

    async def chatroom_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id).username
        except User.DoesNotExist:
            return "undefined"

    pass

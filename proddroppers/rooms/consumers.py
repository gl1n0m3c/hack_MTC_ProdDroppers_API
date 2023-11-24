import json
from venv import create
from channels.generic.websocket import AsyncWebsocketConsumer
from rooms.models import Rooms, Messages, UsersRooms
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_exists = await self.room_exists(self.room_name)
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        await self.create_user_in_room(self.user_id, self.room_name)
        self.room_group_name = "chat_%s" % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.delete_user_in_room(self.user_id, self.room_name)
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_id = text_data_json["user_id"]
        username = await self.get_user(user_id)
        await self.create_message(user_id, message, self.room_name)
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

    @database_sync_to_async
    def create_message(self, user_id, text, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        Messages.objects.create(user=user, message=text, room=room)

    @database_sync_to_async
    def create_user_in_room(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        try:
            user_in_room = UsersRooms.objects.get(user=user)
        except UsersRooms.DoesNotExist:
            UsersRooms.objects.create(user=user, room=room)
            return
        user_in_room.delete()
        UsersRooms.objects.create(user=user, room=room)

    @database_sync_to_async
    def delete_user_in_room(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        try:
            user_in_room = UsersRooms.objects.get(user=user)
        except UsersRooms.DoesNotExist:
            return
        user_in_room.delete()
        if room.user == user:
            room.delete()

    pass

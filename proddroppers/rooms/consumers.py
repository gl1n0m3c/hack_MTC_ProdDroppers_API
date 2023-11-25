import json
from venv import create
from channels.generic.websocket import AsyncWebsocketConsumer
from rooms.models import Rooms, Messages, UsersRooms
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
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
        audio_time = text_data_json["audio_time"]
        audio_paused = text_data_json["audio_paused"]
        username = await self.get_user(user_id)
        admin = await self.is_admin(user_id, self.room_name)
        msg_date = False
        if message != "":
            msg_date = await self.create_message(
                user_id, message, self.room_name
            )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chatroom_message",
                "message": message,
                "username": username,
                "is_admin": admin,
                "audio_time": audio_time,
                "audio_paused": audio_paused,
                "user_id": user_id,
                "date": msg_date,
            },
        )

    async def chatroom_message(self, event):
        message = event["message"]
        username = event["username"]
        admin = event["is_admin"]
        audio_time = event["audio_time"]
        audio_paused = event["audio_paused"]
        user_id = event["user_id"]
        msg_date = event["date"]
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "is_admin": admin,
                    "audio_time": audio_time,
                    "audio_paused": audio_paused,
                    "user_id": user_id,
                    "date": msg_date,
                }
            )
        )

    @database_sync_to_async
    def is_admin(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return False
        if user == room.user:
            return True
        return False

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id).username
        except User.DoesNotExist:
            return ""

    @database_sync_to_async
    def create_message(self, user_id, text, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return False
        msg = Messages.objects.create(user=user, message=text, room=room)
        return msg.date.strftime("%Y-%m-%d %H:%M:%S")

    @database_sync_to_async
    def create_user_in_room(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        try:
            user_in_room = UsersRooms.objects.get(user=user)
            UsersRooms.objects.get(room=room)
        except UsersRooms.DoesNotExist:
            print("fkjsfwe")
            UsersRooms.objects.create(user=user, room=room)
            return
        print(123)
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

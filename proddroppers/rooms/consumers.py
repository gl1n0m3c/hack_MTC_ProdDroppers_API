import json
from venv import create
from channels.generic.websocket import AsyncWebsocketConsumer
from rooms.models import Rooms, Messages, UsersRooms
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.room_group_name = "chat_%s" % self.room_id
        await self.create_user_in_room(self.user_id, self.room_id)
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        if await self.is_admin(self.user_id, self.room_id):
            await self.delete_user_in_room(self.user_id, self.room_id)
            await self.choose_admin(self.room_id)
        else:
            await self.delete_user_in_room(self.user_id, self.room_id)
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_id = text_data_json["user_id"]
        audio_time = text_data_json["audio_time"]
        audio_paused = text_data_json["audio_paused"]
        delete_room = text_data_json["delete_room"]
        change_admin = text_data_json["change_admin"]
        deleted_room = False
        changed_admin = False
        if delete_room:
            await self.delete_room(self.room_id)
            deleted_room = True
        elif change_admin:
            await self.change_admin_by_request(user_id, self.room_id)
            changed_admin = True
        username = await self.get_user(user_id)
        admin = await self.is_admin(user_id, self.room_id)
        admin_username = await self.get_admin_username(self.room_id)
        msg_date = False
        if message != "":
            msg_date = await self.create_message(
                user_id, message, self.room_id
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
                "changed_admin": changed_admin,
                "deleted_room": deleted_room,
                "admin_username": admin_username,
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
        deleted_room = event["deleted_room"]
        changed_admin = event["changed_admin"]
        admin_username = event["admin_username"]
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
                    "changed_admin": changed_admin,
                    "deleted_room": deleted_room,
                    "admin_username": admin_username,
                }
            )
        )

    @database_sync_to_async
    def change_admin_by_request(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        try:
            uir_admin = UsersRooms.objects.get(
                room=room, user=user, is_admin=True
            )
            uir_default = UsersRooms.objects.get(room=room, is_admin=False)
        except UsersRooms.DoesNotExist:
            return
        uir_admin.is_admin = False
        uir_admin.save()
        uir_default.is_admin = True
        uir_default.save()

    @database_sync_to_async
    def delete_room(self, room_id):
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return
        room.delete()

    @database_sync_to_async
    def is_admin(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return False
        try:
            user_in_room = UsersRooms.objects.get(user=user, room=room)
        except UsersRooms.DoesNotExist:
            return False
        return user_in_room.is_admin

    @database_sync_to_async
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id).username
        except User.DoesNotExist:
            return ""

    @database_sync_to_async
    def get_admin_username(self, room_id):
        try:
            room = Rooms.objects.get(id=room_id)
            return UsersRooms.objects.get(
                is_admin=True,
                room=room,
            ).user.username
        except (
            Rooms.DoesNotExist,
            UsersRooms.DoesNotExist,
        ):
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
        user_in_room = UsersRooms.objects.filter(user=user)
        user_in_room1 = UsersRooms.objects.filter(room=room, is_admin=True)
        if len(user_in_room) == 0 and len(user_in_room1) == 0:
            UsersRooms.objects.create(user=user, room=room, is_admin=True)
            return
        elif len(user_in_room) == 0:
            UsersRooms.objects.create(
                user=user,
                room=room,
            )
            return
        for uir in user_in_room:
            uir.delete()
        try:
            UsersRooms.objects.get(room=room, is_admin=True)
        except UsersRooms.DoesNotExist:
            UsersRooms.objects.create(user=user, room=room, is_admin=True)
            return
        UsersRooms.objects.create(user=user, room=room)

    @database_sync_to_async
    def delete_user_in_room(self, user_id, room_id):
        try:
            user = User.objects.get(id=user_id)
            room = Rooms.objects.get(id=room_id)
        except (User.DoesNotExist, Rooms.DoesNotExist):
            return
        try:
            user_in_room = UsersRooms.objects.get(user=user, room=room)
        except UsersRooms.DoesNotExist:
            return
        user_in_room.delete()

    @database_sync_to_async
    def choose_admin(self, room_id):
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return
        try:
            uir = UsersRooms.objects.get(room=room)
        except UsersRooms.DoesNotExist:
            return
        uir.is_admin = True
        uir.save()

    pass

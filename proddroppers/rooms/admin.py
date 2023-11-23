from django.contrib import admin
from rooms.models import Messages, Rooms, UsersRooms


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = [
        Rooms.name.field.name,
        Rooms.user.field.name,
        Rooms.current.field.name,
    ]
    readonly_fields = [
        Rooms.user.field.name,
        Rooms.current.field.name,
    ]


@admin.register(UsersRooms)
class UsersRoomsAdmin(admin.ModelAdmin):
    list_display = [
        UsersRooms.user.field.name,
        UsersRooms.room.field.name,
    ]


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = [
        Messages.room.field.name,
        Messages.user.field.name,
        Messages.message.field.name,
        Messages.date.field.name,
    ]
    readonly_fields = [
        Messages.room.field.name,
        Messages.user.field.name,
    ]

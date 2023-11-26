from django.contrib.auth.models import User
from django.db import models

from core.models import AbstractNameModel
from users_music.models import Music


class UsersRoomsManager(models.Manager):
    def get_users_in_room(self, room_id):
        return (
            self.get_queryset()
            .select_related(UsersRooms.user.field.name)
            .filter(room=room_id)
            .only(
                f"{UsersRooms.user.field}__{User.username.field.name}",
                UsersRooms.is_admin.field.name,
            )
        )


class Rooms(AbstractNameModel):
    current = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="музыка",
        related_name="rooms",
    )

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"

    def __str__(self):
        return self.name


class UsersRooms(models.Model):
    objects = UsersRoomsManager()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        related_name="room",
    )

    is_admin = models.BooleanField(
        verbose_name="является ли администратором",
        default=False,
    )

    room = models.ForeignKey(
        Rooms,
        on_delete=models.CASCADE,
        verbose_name="комната",
        related_name="room",
    )

    class Meta:
        verbose_name = "пользователь в комнате"
        verbose_name_plural = "пользователи в комнатах"

    def __str__(self):
        return str(self.user)


class Messages(models.Model):
    room = models.ForeignKey(
        Rooms,
        on_delete=models.CASCADE,
        verbose_name="комната",
        related_name="комнаты",
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        related_name="messages",
    )

    message = models.TextField(verbose_name="сообщение")

    date = models.DateTimeField(
        auto_now=True,
        verbose_name="дата",
    )

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return str(self.user)

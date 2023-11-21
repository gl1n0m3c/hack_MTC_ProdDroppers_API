from django.contrib.auth.models import User
from django.db import models

from core.models import AbstractNameModel
from users_music.models import Music


class Rooms(AbstractNameModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="админ",
        related_name="rooms",
    )

    current = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        verbose_name="музыка",
        related_name="rooms",
    )

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"

    def __str__(self):
        return self.name


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

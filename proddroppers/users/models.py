from django.contrib.auth.models import User
from django.db import models

from users_music.models import Music


class FriendsAsseptedManaget(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related(FriendsAssepted.user2.field.name)
            .filter(user1=pk)
            .only(
                f"{FriendsAssepted.user2.field.name}"
                + "__"
                + f"{User.username.field.name}",
            )
        )


class FriendsNotAsseptedManaget(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related(FriendsNotAssepted.user2.field.name)
            .filter(user1=pk)
            .only(
                f"{FriendsNotAssepted.user2.field.name}"
                + "__"
                + f"{User.username.field.name}",
            )
        )


class FriendsAssepted(models.Model):
    objects = FriendsAsseptedManaget()

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="отправил",
        related_name="friend_requests_sent_assepted",
    )

    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friend_requests_received_assepted",
    )

    class Meta:
        verbose_name = "подтвержденный друг"
        verbose_name_plural = "подтвержденные друзья"

    def __str__(self):
        return str(self.user1)


class FriendsNotAssepted(models.Model):
    objects = FriendsNotAsseptedManaget()

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="отправил",
        related_name="friend_requests_sent_not_assepted",
    )

    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="получил",
        related_name="friend_requests_received_not_assepted",
    )

    class Meta:
        verbose_name = "не подтвержденный друг"
        verbose_name_plural = "не подтвержденные друзья"

    def __str__(self):
        return str(self.user1)


class UserMusic(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_music",
        verbose_name="Пользователь",
    )

    music = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        related_name="user_music",
        verbose_name="Музыка",
    )

    class Meta:
        verbose_name = "связь пользователя и музыки"
        verbose_name_plural = "связи пользователей и музыки"

    def __str__(self):
        return str(self.user)

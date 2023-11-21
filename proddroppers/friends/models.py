from django.contrib.auth.models import User
from django.db import models

from users.models import UserNewFields


class FriendsAsseptedManager(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related(
                f"{FriendsAssepted.user2.field.name}__new_fields",
            )
            .filter(user1=pk)
            .only(
                f"{FriendsAssepted.user2.field.name}"
                + "__"
                + f"{User.username.field.name}",
                f"{FriendsAssepted.user2.field.name}"
                + "__new_fields__"
                + f"{UserNewFields.image.field.name}",
            )
        )


class FriendsNotAsseptedManager(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related(
                f"{FriendsNotAssepted.user1.field.name}__new_fields",
            )
            .filter(user2=pk)
            .only(
                f"{FriendsNotAssepted.user1.field.name}"
                + "__"
                + f"{User.username.field.name}",
                f"{FriendsNotAssepted.user1.field.name}"
                + "__new_fields__"
                + f"{UserNewFields.image.field.name}",
            )
        )


class FriendsAssepted(models.Model):
    objects = FriendsAsseptedManager()

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        related_name="friend_requests_sent_assepted",
    )

    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="его подтвержденный друг",
        related_name="friend_requests_received_assepted",
    )

    class Meta:
        verbose_name = "подтвержденный друг"
        verbose_name_plural = "подтвержденные друзья"

    def __str__(self):
        return str(self.user1)


class FriendsNotAssepted(models.Model):
    objects = FriendsNotAsseptedManager()

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

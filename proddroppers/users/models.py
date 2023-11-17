from django.contrib.auth.models import User
from django.db import models


class FriendsAssepted(models.Model):
    id1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="отправил",
        related_name="friend_requests_sent_assepted",
    )

    id2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="friend_requests_received_assepted",
    )

    class Meta:
        verbose_name = "подтвержденный друг"
        verbose_name_plural = "подтвержденные друзья"

    def __str__(self):
        return str(self.id1)


class FriendsNotAssepted(models.Model):
    id1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="отправил",
        related_name="friend_requests_sent_not_assepted",
    )

    id2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="получил",
        related_name="friend_requests_received_not_assepted",
    )

    class Meta:
        verbose_name = "не подтвержденный друг"
        verbose_name_plural = "не подтвержденные друзья"

    def __str__(self):
        return str(self.id1)

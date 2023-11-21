from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from sorl.thumbnail import delete

from core.models import ImageOperations
from users_music.models import Music


class FriendsAsseptedManager(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related("user1", "user2", "user2__usernewfields")
            .filter(user1=pk)
            .only(
                "user1__username",
                "user2__username",
                "user2__usernewfields__image",
            )
        )


class FriendsNotAsseptedManager(models.Manager):
    def get_friends(self, pk):
        return (
            self.get_queryset()
            .select_related(FriendsNotAssepted.user1.field.name)
            .filter(user2=pk)
            .only(
                f"{FriendsNotAssepted.user1.field.name}__{User.username.field.name}",
                f"{FriendsNotAssepted.user1.field.name}__{User.usernewfields.field.name}__{UserNewFields.image.field.name}",
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


class UserNewFields(models.Model, ImageOperations):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="new_fields",
        verbose_name="пользователь",
    )

    image = models.ImageField(
        upload_to="images/users/",
        verbose_name="аватарка",
        default="default/default_user_image.png/",
        null=True,
        blank=True,
    )

    music = models.ManyToManyField(
        Music,
        related_name="added_fields",
        verbose_name="музыка",
        blank=True,
    )

    class Meta:
        verbose_name = "дополнительное поле"
        verbose_name_plural = "дополнительные поля"

    def __str__(self):
        return str(self.user)


@receiver(pre_delete, sender=UserNewFields)
def sorl_delete(sender, instance, **kwargs):
    if instance.image != "default/default_user_image.png":
        delete(instance.image)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserNewFields.objects.create(user=instance)

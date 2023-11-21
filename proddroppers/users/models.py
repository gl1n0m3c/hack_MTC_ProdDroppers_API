from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from sorl.thumbnail import delete

from core.models import ImageOperations
from users_music.models import Music


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

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from sorl.thumbnail import delete, get_thumbnail

from core.models import AbstractNameModel


class Artist(AbstractNameModel):
    class Meta:
        verbose_name = "артист"
        verbose_name_plural = "артисты"

    def __str__(self):
        return self.name


class Albom(AbstractNameModel):
    artist = models.ForeignKey(
        Artist,
        verbose_name="исполнитель",
        on_delete=models.CASCADE,
        related_name="music",
    )

    music_image = models.ImageField(
        upload_to="images/music/",
        verbose_name="обложка музыкального файла",
        default="default/default_music_image.png",
    )

    def get_image_300x300(self):
        return get_thumbnail(self.music_image, "300x300", quality=51)

    def display_image(self):
        return mark_safe(
            f"<img src='{self.get_image_300x300().url}' width=50>",
        )

    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"

    def __str__(self):
        return self.name

    display_image.short_description = "превью"
    display_image.allow_tags = True


class Category(AbstractNameModel):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Music(AbstractNameModel):
    category = models.ForeignKey(
        Category,
        verbose_name="категория",
        on_delete=models.CASCADE,
        related_name="music",
    )

    albom = models.ForeignKey(
        Albom,
        verbose_name="альбом",
        on_delete=models.CASCADE,
        related_name="music",
    )

    music_file = models.FileField(
        upload_to="music/",
        verbose_name="музыкальный файл",
    )

    class Meta:
        verbose_name = "музыка"
        verbose_name_plural = "музыка"

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Music)
def sorl_delete(sender, instance, **kwargs):
    delete(instance.music_file)


@receiver(pre_delete, sender=Albom)
def sorl_delete(sender, instance, **kwargs):
    if instance.music_image != "default/default_music_image.png":
        delete(instance.music_image)

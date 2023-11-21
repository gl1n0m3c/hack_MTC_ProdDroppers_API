from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from sorl.thumbnail import delete

from core.models import AbstractNameModel, ImageOperations


class Artist(AbstractNameModel):
    class Meta:
        verbose_name = "артист"
        verbose_name_plural = "артисты"

    def __str__(self):
        return self.name


class Albom(AbstractNameModel, ImageOperations):
    artist = models.ForeignKey(
        Artist,
        verbose_name="исполнитель",
        on_delete=models.CASCADE,
        related_name="music",
    )

    image = models.ImageField(
        upload_to="images/music/",
        verbose_name="обложка музыкального файла",
        default="default/default_music_image.png",
    )

    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"

    def __str__(self):
        return self.name


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
        validators=[
            FileExtensionValidator(allowed_extensions=["mp3", "wav", "ogg"]),
        ],
    )

    class Meta:
        verbose_name = "музыка"
        verbose_name_plural = "музыка"

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Music)
@receiver(pre_delete, sender=Albom)
def sorl_delete(sender, instance, **kwargs):
    if isinstance(instance, Music):
        delete(instance.music_file)
    else:
        if instance.music_image != "default/default_music_image.png":
            delete(instance.music_image)

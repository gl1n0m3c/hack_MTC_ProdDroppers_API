import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from sorl.thumbnail import delete

from core.models import AbstractNameModel, ImageOperations


class MusicManager(models.Manager):
    def get_one_music(self, pk):
        return (
            self.get_queryset()
            .select_related(
                Music.albom.field.name,
                f"{Music.albom.field.name}__{Albom.artist.field.name}",
            )
            .filter(pk=pk)
            .only(
                Music.name.field.name,
                f"{Music.albom.field.name}__{Albom.artist.field.name}__{Artist.name.field.name}",
                f"{Music.albom.field.name}__{Albom.image.field.name}",
                Music.music_file.field.name,
            )
        )

    def get_many_music(self, start):
        return (
            self.get_queryset()
            .select_related(
                Music.albom.field.name,
                f"{Music.albom.field.name}__{Albom.artist.field.name}",
            )
            .filter(name__startswith=start)
            .only(
                Music.name.field.name,
                f"{Music.albom.field.name}__{Albom.artist.field.name}__{Artist.name.field.name}",
                f"{Music.albom.field.name}__{Albom.image.field.name}",
                Music.music_file.field.name,
            )
            .order_by(Music.name.field.name)
        )


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


class Mood(AbstractNameModel):
    class Meta:
        verbose_name = "настроение"
        verbose_name_plural = "настроения"

    def __str__(self):
        return self.name


class Music(AbstractNameModel):
    objects = MusicManager()

    def _image_upload_path(self, filename):
        file_extension = filename.split(".")[-1]
        return f"music/{uuid.uuid4().hex}.{file_extension}"

    category = models.ForeignKey(
        Category,
        verbose_name="категория",
        on_delete=models.CASCADE,
        related_name="music",
    )

    mood = models.ManyToManyField(
        Mood,
        verbose_name="настроение",
        related_name="music",
    )

    albom = models.ForeignKey(
        Albom,
        verbose_name="альбом",
        on_delete=models.CASCADE,
        related_name="music",
    )

    music_file = models.FileField(
        upload_to=_image_upload_path,
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

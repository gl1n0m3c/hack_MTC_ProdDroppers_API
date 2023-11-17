from django.db import models


class Category(models.Model):
    name = models.TextField(
        unique=True,
        verbose_name="название",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.TextField(
        unique=True,
        verbose_name="название",
    )

    category = models.ForeignKey(
        Category,
        verbose_name="категория",
        on_delete=models.CASCADE,
        related_name="music",
    )

    music_file = models.FileField(
        upload_to="music/",
        verbose_name="музыкальный файл",
    )

    music_image = models.ImageField(
        upload_to="images/music/",
        verbose_name="обложка музыкального файла",
    )

    class Meta:
        verbose_name = "музыка"
        verbose_name_plural = "музыка"

    def __str__(self):
        return self.name

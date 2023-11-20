from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class AbstractNameModel(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="название",
    )

    class Meta:
        abstract = True


class ImageOperations:
    def get_image_300x300(self):
        return get_thumbnail(self.image, "300x300", quality=51)

    def display_image(self):
        return mark_safe(
            f"<img src='{self.get_image_300x300().url}' width=50>",
        )

    display_image.short_description = "превью"
    display_image.allow_tags = True

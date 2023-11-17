from django.db import models


class AbstractNameModel(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="название",
    )

    class Meta:
        abstract = True

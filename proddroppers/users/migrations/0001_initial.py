# Generated by Django 4.2.7 on 2023-11-21 12:52

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users_music", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserNewFields",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default/default_user_image.png/",
                        null=True,
                        upload_to="images/users/",
                        verbose_name="аватарка",
                    ),
                ),
                (
                    "music",
                    models.ManyToManyField(
                        blank=True,
                        related_name="added_fields",
                        to="users_music.music",
                        verbose_name="музыка",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="new_fields",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "дополнительное поле",
                "verbose_name_plural": "дополнительные поля",
            },
            bases=(models.Model, core.models.ImageOperations),
        ),
        migrations.CreateModel(
            name="FriendsNotAssepted",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_sent_not_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="отправил",
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_received_not_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="получил",
                    ),
                ),
            ],
            options={
                "verbose_name": "не подтвержденный друг",
                "verbose_name_plural": "не подтвержденные друзья",
            },
        ),
        migrations.CreateModel(
            name="FriendsAssepted",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_sent_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_received_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="его подтвержденный друг",
                    ),
                ),
            ],
            options={
                "verbose_name": "подтвержденный друг",
                "verbose_name_plural": "подтвержденные друзья",
            },
        ),
    ]

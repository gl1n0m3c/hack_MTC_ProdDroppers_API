from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                    "id1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_sent_not_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="отправил",
                    ),
                ),
                (
                    "id2",
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
                    "id1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_sent_assepted",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="отправил",
                    ),
                ),
                (
                    "id2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friend_requests_received_assepted",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "подтвержденный друг",
                "verbose_name_plural": "подтвержденные друзья",
            },
        ),
    ]

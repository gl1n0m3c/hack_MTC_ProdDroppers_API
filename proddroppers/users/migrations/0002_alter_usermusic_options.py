# Generated by Django 4.2.7 on 2023-11-18 22:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usermusic",
            options={
                "verbose_name": "связь пользователя и музыки",
                "verbose_name_plural": "связи пользователей и музыки",
            },
        ),
    ]
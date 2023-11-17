from django.contrib import admin

from users_music.models import Category, Music


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        Category.name.field.name,
    ]


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = [
        Music.name.field.name,
        Music.category.field.name,
    ]
    # СДЕЛАТЬ КРАСИВЫЙ ВЫВОД ФАЙЛИКА

from django.contrib import admin

from users_music.models import Albom, Artist, Category, Music


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = [Artist.name.field.name]


@admin.register(Albom)
class AlbomAdmin(admin.ModelAdmin):
    list_display = [
        Albom.name.field.name,
        Albom.artist.field.name,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [Category.name.field.name]


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = [
        Music.name.field.name,
        Music.category.field.name,
        Music.albom.field.name,
        Music.display_image,
    ]

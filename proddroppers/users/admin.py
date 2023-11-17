from django.contrib import admin

from users.models import FriendsAssepted, FriendsNotAssepted


@admin.register(FriendsAssepted)
class FriendsAsseptedAdmin(admin.ModelAdmin):
    list_display = [
        FriendsAssepted.id1.field.name,
        FriendsAssepted.id2.field.name,
    ]


@admin.register(FriendsNotAssepted)
class FriendsNotAsseptedAdmin(admin.ModelAdmin):
    list_display = [
        FriendsNotAssepted.id1.field.name,
        FriendsNotAssepted.id2.field.name,
    ]

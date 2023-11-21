from django.contrib import admin

from friends.models import FriendsAssepted, FriendsNotAssepted


@admin.register(FriendsAssepted)
class FriendsAsseptedAdmin(admin.ModelAdmin):
    list_display = [
        FriendsAssepted.user1.field.name,
        FriendsAssepted.user2.field.name,
    ]


@admin.register(FriendsNotAssepted)
class FriendsNotAsseptedAdmin(admin.ModelAdmin):
    list_display = [
        FriendsNotAssepted.user1.field.name,
        FriendsNotAssepted.user2.field.name,
    ]

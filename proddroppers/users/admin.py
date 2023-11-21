from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import (
    FriendsAssepted,
    FriendsNotAssepted,
    UserNewFields,
)


class NewFieldsInline(admin.TabularInline):
    model = UserNewFields
    can_delete = False


class NewUserAdmin(UserAdmin):
    inlines = [NewFieldsInline]


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


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

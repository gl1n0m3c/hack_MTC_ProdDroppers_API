from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import UserNewFields


class NewFieldsInline(admin.TabularInline):
    model = UserNewFields
    can_delete = False


class NewUserAdmin(UserAdmin):
    inlines = [NewFieldsInline]


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(UserNewFields)

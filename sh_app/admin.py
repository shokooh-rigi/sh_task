from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.action(description='رفع محدودیت')
def release_blocked_user(modeladmin, request, queryset):
    queryset.update(is_active=True)


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active')
    actions = [release_blocked_user]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

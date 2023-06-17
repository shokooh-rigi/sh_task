from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.urls import reverse


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'release_user')

    def release_user(self, obj):
        if not obj.is_active:
            return '<a href="{}">رفع محدودیت</a>'.format(reverse('admin:release_user') + '?username=' + obj.username)
        else:
            return '-'
    release_user.short_description = 'رفع محدودیت'
    release_user.allow_tags = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

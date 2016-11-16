from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Myuser


class UserAdmin(BaseUserAdmin):

    fieldsets = BaseUserAdmin.fieldsets + (
        ('My info', {'fields': ('username', 'avatar')}),
    )

    def admin_avatar(self, instance):
        return instance.avatar and u'<img src="/static/avatar.jpg" width="100px" />'.format(
            instance.avatar.url
        )
    admin_avatar.allow_tags = True
    admin_avatar.short_description = 'Avatar'


admin.site.register(Myuser, UserAdmin)

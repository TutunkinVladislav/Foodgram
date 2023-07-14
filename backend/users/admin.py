from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'username')


admin.site.register(User, UserAdmin)

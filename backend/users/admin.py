from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
        'count_subscribe',
        'count_recipe',
    )
    readonly_fields = (
        'count_subscribe',
        'count_recipe',
    )
    list_filter = ('email', 'username')

    def count_subscribe(self, obj):
        return obj.follower.count()

    count_subscribe.short_description = 'Подписки'

    def count_recipe(self, obj):
        return obj.recipe.count()

    count_recipe.short_description = 'Рецепты'


admin.site.register(User, UserAdmin)

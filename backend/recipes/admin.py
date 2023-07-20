from django.contrib import admin

from .models import (FavoriteRecipe, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Subscribe, Tag)


class IngredientsInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 3


class TagsInline(admin.TabularInline):
    model = Recipe.tags.through
    extra = 3


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'count_favorite',
    )
    exclude = ('tags',)
    readonly_fields = ('count_favorite',)
    inlines = (IngredientsInline, TagsInline,)
    search_fields = ('name', 'author', 'tags')
    list_filter = ('name', 'author', 'tags')
    empty_value_display = '-пусто-'

    def count_favorite(self, obj):
        return obj.favorite.count()

    count_favorite.short_description = 'Добавлено в избранное'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(IngredientAmount)
admin.site.register(FavoriteRecipe)
admin.site.register(Subscribe)
admin.site.register(ShoppingCart)

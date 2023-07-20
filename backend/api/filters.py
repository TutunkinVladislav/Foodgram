from django_filters.rest_framework import FilterSet, filters

from recipes.models import Ingredient, Recipe


class IngredientFilter(FilterSet):
    """Фильтр для ингредиентов"""
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipesFilter(FilterSet):
    """Фильтр для рецептов"""
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.Filter(field_name='is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_is_in_shopping_cart',
    )

    class Meta:
        model = Recipe
        fields = ['is_favorited', 'author', 'tags', 'is_in_shopping_cart']

    def get_is_in_shopping_cart(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(shopping_cart__user=user)
        return queryset

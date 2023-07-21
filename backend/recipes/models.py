from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User
from .constants import (LENGTH_FIELD_COLOR, LENGTH_FIELD_NAME,
                        ONE_GRAMM_NGREDIENTS, ONE_MINUTES,
                        THREE_HUNDRED_MINUTES,
                        THREE_THOUSANS_GRAMM_INGREDIENTS)


class Ingredient(models.Model):
    """Модель ингредиентов"""

    name = models.CharField(
        verbose_name='Название ингредиента',
        max_length=LENGTH_FIELD_NAME,
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=LENGTH_FIELD_NAME,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('name', 'measurement_unit'),
                name='unique_name_measurement')]
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.measurement_unit})'


class Tag(models.Model):
    """Модель тегов"""

    name = models.CharField(
        verbose_name='Название тега',
        max_length=LENGTH_FIELD_NAME,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цветовой HEX-код',
        max_length=LENGTH_FIELD_COLOR,
        default='#00ff7f',
        null=True,
        blank=True,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Slug тега',
        max_length=LENGTH_FIELD_NAME,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецептов"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipe',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        through='IngredientAmount',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        related_name='recipes',
    )
    image = models.ImageField(
        verbose_name='Изображение рецепта',
        upload_to='recipes/images',
    )
    name = models.CharField(
        verbose_name='Название рецепта',
        max_length=LENGTH_FIELD_NAME,
    )
    text = models.TextField(
        verbose_name='Описание рецепта',
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        default=ONE_MINUTES,
        validators=(MinValueValidator(ONE_MINUTES, 'Минимум 1 минута'),
                    MaxValueValidator(THREE_HUNDRED_MINUTES,
                                      'Максимум 300 минут')),
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации рецепта',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return f'Автор: {self.author.username} рецепт: {self.name}'


class IngredientAmount(models.Model):
    """Модель для количества ингредиентов"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        default=ONE_GRAMM_NGREDIENTS,
        validators=(MinValueValidator(ONE_GRAMM_NGREDIENTS, 'Минимум 1г.'),
                    MaxValueValidator(THREE_THOUSANS_GRAMM_INGREDIENTS,
                                      'Максимум 3000г.')),
    )

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(
                fields=('recipe', 'ingredient'),
                name='unique ingredient')]

    def __str__(self):
        return (f'В рецепте {self.recipe.name} {self.amount} '
                f'{self.ingredient.measurement_unit} {self.ingredient.name}')


class AbstractBase(models.Model):
    """Абстрактная модель"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique favourite')]


class FavoriteRecipe(AbstractBase):
    """Модель избранных рецептов"""

    class Meta:
        default_related_name = 'favorite'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return (f'Пользователь: {self.user.username}'
                f'рецепт: {self.recipe.name}')


class ShoppingCart(AbstractBase):
    """Модель списка покупок"""

    class Meta:
        default_related_name = 'shopping_cart'
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'

    def __str__(self):
        return (f'Пользователь: {self.user.username},'
                f'рецепт в списке: {self.recipe.name}')


class Subscribe(models.Model):
    """Модель подписок"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )
    created = models.DateTimeField(
        verbose_name='Дата подписки',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-created',)
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription')]

    def __str__(self):
        return (f'Пользователь: {self.user.username},'
                f' автор: {self.author.username}')

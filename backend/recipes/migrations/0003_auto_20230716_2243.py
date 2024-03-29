# Generated by Django 3.2.16 on 2023-07-16 19:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriterecipe',
            options={'default_related_name': 'favorite', 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранные'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'default_related_name': 'shopping_cart', 'verbose_name': 'Список покупок', 'verbose_name_plural': 'Список покупок'},
        ),
        migrations.RemoveConstraint(
            model_name='favoriterecipe',
            name='unique favourite',
        ),
        migrations.RemoveConstraint(
            model_name='shoppingcart',
            name='unique recipe in shopping cart',
        ),
        migrations.RemoveField(
            model_name='favoriterecipe',
            name='favorite_recipe',
        ),
        migrations.AddField(
            model_name='favoriterecipe',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='ingredientamount',
            name='amount',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1'), django.core.validators.MaxValueValidator(15, 'Максимум 15')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1 минута'), django.core.validators.MaxValueValidator(180, 'Максимум 3 часа')], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]

# Generated by Django 3.2.16 on 2023-07-21 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20230717_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='ingredientamount',
            options={'ordering': ('recipe',), 'verbose_name': 'Количество ингредиента', 'verbose_name_plural': 'Количество ингредиентов'},
        ),
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ('-created',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AlterField(
            model_name='ingredientamount',
            name='amount',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1г.'), django.core.validators.MaxValueValidator(3000, 'Максимум 3000г.')], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, 'Минимум 1 минута'), django.core.validators.MaxValueValidator(300, 'Максимум 300 минут')], verbose_name='Время приготовления'),
        ),
    ]

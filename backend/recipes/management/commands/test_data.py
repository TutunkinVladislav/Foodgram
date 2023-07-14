import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        with open(
            'E:/Dev/foodgram-project-react/data/ingredients.csv',
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            try:
                Ingredient.objects.bulk_create(
                    Ingredient(**items) for items in reader
                )
            except IntegrityError:
                return 'Такие ингредиенты уже есть...'
        return (
            f'{Ingredient.objects.count()} - ингредиентов успешно загружено')

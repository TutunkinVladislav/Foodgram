from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import LENGTH_EMAIL, LENGTH_FIELD


class User(AbstractUser):
    """Модель пользователей"""

    email = models.EmailField(
        verbose_name='Email',
        max_length=LENGTH_EMAIL,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Логин',
        max_length=LENGTH_FIELD,
        unique=True,
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=LENGTH_FIELD,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=LENGTH_FIELD,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=LENGTH_FIELD,
    )

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

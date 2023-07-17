from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import LENGTH_EMAIL, LENGTH_FIELD, LENGTH_ROLE


class User(AbstractUser):
    """Модель пользователей"""

    ADMIN = 'admin'
    AUTHORIZED = 'authorized'
    GUEST = 'guest'
    ROLES = (
        (ADMIN, 'admin'),
        (AUTHORIZED, 'authorized'),
        (GUEST, 'guest'),
    )

    email = models.EmailField(
        'Email',
        max_length=LENGTH_EMAIL,
        unique=True,
    )
    username = models.CharField(
        'Логин',
        max_length=LENGTH_FIELD,
        unique=True,
    )
    password = models.CharField(
        'Пароль',
        max_length=LENGTH_FIELD,
    )
    first_name = models.CharField(
        'Имя',
        max_length=LENGTH_FIELD,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=LENGTH_FIELD,
    )
    role = models.CharField(
        'Роль',
        default=GUEST,
        choices=ROLES,
        max_length=LENGTH_ROLE,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_guest(self):
        return self.role == self.GUEST

    @property
    def is_authorized(self):
        return self.role == self.AUTHORIZED

    @property
    def is_admin(self):
        return self.role == self.ADMIN

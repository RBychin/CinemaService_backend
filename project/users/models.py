from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    telegram_id = models.BigIntegerField(
        unique=True,
        blank=False,
        null=False,
        verbose_name='Telegram ID'
    )
    department = models.ForeignKey(
        'core.Department',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='департамент'
    )


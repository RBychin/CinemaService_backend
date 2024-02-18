from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Department(models.Model):
    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'департаменты'

    name = models.CharField(
        max_length=120,
        verbose_name='Название департамента'
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    name = models.CharField(
        max_length=250,
        verbose_name='название проекта'
    )
    shift_duration = models.PositiveIntegerField(
        verbose_name='продолжительность смены (ч)'
    )
    shift_non_sleep_duration = models.PositiveIntegerField(
        verbose_name='разрвы между сменами (ч)'
    )
    shift_salary = models.PositiveIntegerField(
        verbose_name='стоимость смены (р)'
    )
    overtime_salary = models.PositiveIntegerField(
        verbose_name='стоимость часа переработки (ч)'
    )
    non_sleep_salary = models.PositiveIntegerField(
        verbose_name='стоимость часа недосыпа (ч)'
    )
    later_lunch_salary = models.PositiveIntegerField(
        verbose_name='стоимость позднего обеда (р)'
    )
    current_lunch_salary = models.PositiveIntegerField(
        verbose_name='стоимость текущего обеда (р)'
    )
    daily_expenses = models.PositiveIntegerField(
        verbose_name='суточные (р)'
    )
    day_off = models.PositiveIntegerField(
        verbose_name='day off (р)'
    )
    camervagen_salary = models.PositiveIntegerField(
        verbose_name='аренда камервагена (р)'
    )
    camervagen_odo_salary = models.PositiveIntegerField(
        verbose_name='стоимость пробега за км'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='активен'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='проект создан'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name='проект пользователя'
    )

    def __str__(self):
        return self.name


class Shift(models.Model):
    class Meta:
        verbose_name = 'смена'
        verbose_name_plural = 'смены'

    start_time = models.DateTimeField(
        verbose_name='начало смены'
    )
    stop_time = models.DateTimeField(
        verbose_name='окончание смены'
    )
    current_lunch = models.BooleanField(
        default=False,
        verbose_name='текущий обед'
    )
    camervagen_odo = models.PositiveIntegerField(
        default=0,
        verbose_name='пробег камервагена (км)'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='создана смена'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shifts',
        verbose_name='смена пользователя'
    )

    def __str__(self):
        return f'смена от {self.create_date} | {self.user.username}'


class ShiftServices(models.Model):
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    name = models.CharField(
        max_length=150,
        verbose_name='название услуги'
    )
    description = models.TextField(
        max_length=600,
        verbose_name='описание услуги',
        blank=True,
        null=True
    )
    salary = models.PositiveIntegerField(
        verbose_name='стоимость услуги (р)'
    )
    shift = models.ForeignKey(
        Shift,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='смена'
    )

    def __str__(self):
        return self.name
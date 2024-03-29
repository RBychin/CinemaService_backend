# Generated by Django 5.0.2 on 2024-02-18 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название проекта')),
                ('shift_duration', models.PositiveIntegerField(verbose_name='продолжительность смены (ч)')),
                ('shift_non_sleep_duration', models.PositiveIntegerField(verbose_name='разрвы между сменами (ч)')),
                ('shift_salary', models.PositiveIntegerField(verbose_name='стоимость смены (р)')),
                ('overtime_salary', models.PositiveIntegerField(verbose_name='стоимость часа переработки (ч)')),
                ('non_sleep_salary', models.PositiveIntegerField(verbose_name='стоимость часа недосыпа (ч)')),
                ('later_lunch_salary', models.PositiveIntegerField(verbose_name='стоимость позднего обеда (р)')),
                ('current_lunch_salary', models.PositiveIntegerField(verbose_name='стоимость текущего обеда (р)')),
                ('daily_expenses', models.PositiveIntegerField(verbose_name='суточные (р)')),
                ('day_off', models.PositiveIntegerField(verbose_name='day off (р)')),
                ('camervagen_salary', models.PositiveIntegerField(verbose_name='аренда камервагена (р)')),
                ('camervagen_odo_salary', models.PositiveIntegerField(verbose_name='стоимость пробега за км')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='проекты пользователя')),
            ],
        ),
    ]

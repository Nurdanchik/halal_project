# Generated by Django 5.2 on 2025-05-29 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="card",
            name="start_work",
        ),
        migrations.RemoveField(
            model_name="card",
            name="stops_work",
        ),
        migrations.RemoveField(
            model_name="card",
            name="video",
        ),
        migrations.RemoveField(
            model_name="card",
            name="work_days",
        ),
        migrations.CreateModel(
            name="CardWorkDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "dayoftheweek",
                    models.CharField(
                        choices=[
                            ("Monday", "Понедельник"),
                            ("Tuesday", "Вторник"),
                            ("Wednesday", "Среда"),
                            ("Thursday", "Четверг"),
                            ("Friday", "Пятница"),
                            ("Saturday", "Суббота"),
                            ("Sunday", "Воскресенье"),
                        ],
                        max_length=10,
                        verbose_name="День недели",
                    ),
                ),
                ("starts_work", models.TimeField(verbose_name="Время открытия")),
                ("stops_work", models.TimeField(verbose_name="Время закрытия")),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_days",
                        to="cards.card",
                        verbose_name="Карточка",
                    ),
                ),
            ],
            options={
                "verbose_name": "День работы",
                "verbose_name_plural": "Дни работы",
            },
        ),
    ]

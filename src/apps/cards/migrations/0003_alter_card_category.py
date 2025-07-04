# Generated by Django 5.2 on 2025-06-04 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_remove_card_start_work_remove_card_stops_work_and_more"),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cards",
                to="categories.category",
                verbose_name="Категория",
            ),
        ),
    ]

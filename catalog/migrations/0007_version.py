# Generated by Django 5.0.5 on 2024-05-28 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("version", models.PositiveIntegerField(verbose_name="номер версии")),
                (
                    "version_title",
                    models.CharField(max_length=100, verbose_name="название версии"),
                ),
                (
                    "version_mark",
                    models.BooleanField(
                        default=True, verbose_name="признак текущей версии"
                    ),
                ),
                (
                    "name_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="название продукта продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
            },
        ),
    ]

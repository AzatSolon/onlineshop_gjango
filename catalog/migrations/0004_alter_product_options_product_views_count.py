# Generated by Django 5.0.5 on 2024-05-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_remove_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": [
                    "category",
                    "name",
                    "price",
                    "data_make",
                    "data_last_save",
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="views_count",
            field=models.PositiveIntegerField(default=0, verbose_name="Просмотры"),
        ),
    ]

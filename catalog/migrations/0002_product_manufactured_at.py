# Generated by Django 5.0.5 on 2024-05-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                blank=True, null=True, verbose_name="дата производства"
            ),
        ),
    ]

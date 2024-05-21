# Generated by Django 5.0.5 on 2024-05-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="slug"
                    ),
                ),
                ("content", models.TextField(verbose_name="содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/image",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время создания"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(default=0, verbose_name="просмотры"),
                ),
            ],
            options={
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]

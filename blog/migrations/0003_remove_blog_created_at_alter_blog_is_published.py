# Generated by Django 5.0.5 on 2024-05-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_content_alter_blog_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="опубликовано"),
        ),
    ]
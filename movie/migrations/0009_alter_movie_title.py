# Generated by Django 5.0 on 2024-01-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_remove_movie_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]

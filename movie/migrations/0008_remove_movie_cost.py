# Generated by Django 5.0 on 2024-01-08 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cost',
        ),
    ]

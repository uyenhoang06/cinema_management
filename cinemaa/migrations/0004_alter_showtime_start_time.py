# Generated by Django 5.0 on 2023-12-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaa', '0003_alter_showtime_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
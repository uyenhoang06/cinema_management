# Generated by Django 5.0 on 2024-01-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaa', '0009_alter_showtime_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='showtime',
            unique_together={('hall', 'start_time', 'end_time')},
        ),
    ]

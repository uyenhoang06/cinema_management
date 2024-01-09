# Generated by Django 5.0 on 2024-01-07 08:00

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_booking_created_at'),
        ('cinemaa', '0012_remove_seat_status_showtimeseat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 8, 0, 37, 268221, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaa.showtimeseat'),
        ),
    ]

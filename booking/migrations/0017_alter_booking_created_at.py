# Generated by Django 5.0 on 2024-01-08 08:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_booking_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 8, 7, 33, 581236, tzinfo=datetime.timezone.utc)),
        ),
    ]

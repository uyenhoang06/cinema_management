# Generated by Django 5.0 on 2024-01-07 16:48

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_booking_created_at_alter_ticket_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 7, 16, 48, 12, 579235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
    ]

# Generated by Django 5.0 on 2024-01-09 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_remove_booking_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_type',
        ),
    ]

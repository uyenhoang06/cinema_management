# Generated by Django 5.0 on 2023-12-17 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 17), null=True),
        ),
    ]

# Generated by Django 5.0 on 2023-12-21 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customer_membership_alter_customer_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]

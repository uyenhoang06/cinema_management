# Generated by Django 5.0 on 2023-12-22 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaa.halltype'),
        ),
    ]

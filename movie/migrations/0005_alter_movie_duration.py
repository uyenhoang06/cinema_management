# Generated by Django 5.0 on 2023-12-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_customerrating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]

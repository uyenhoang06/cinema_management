# Generated by Django 5.0 on 2023-12-22 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0004_alter_customerrating_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_contact', models.CharField(blank=True, max_length=12, null=True)),
                ('email_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='HallType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('price_surcharge', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShowType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_row', models.IntegerField(blank=True, null=True)),
                ('number_of_column', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable'), ('under_maintenance', 'under_maintenance')], max_length=100)),
                ('cinema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaa.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('slot_status', models.CharField(choices=[('available', 'available'), ('full', 'full'), ('cancelled', 'cancelled')], max_length=50)),
                ('subtitle', models.CharField(choices=[('subtitle', 'subtitle'), ('voice-over', 'voice-over')], max_length=50)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cinemaa.hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.movie')),
            ],
        ),
    ]

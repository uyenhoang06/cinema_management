# Generated by Django 5.0 on 2023-12-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('trailer', models.CharField(blank=True, max_length=100)),
                ('poster', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=3, max_digits=10)),
                ('cost', models.IntegerField(blank=True)),
                ('status', models.BooleanField(blank=True)),
                ('released_year', models.IntegerField(blank=True)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('producer', models.CharField(blank=True, max_length=100)),
                ('language', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2023-12-22 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_schedulestaff_joining_date_alter_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulestaff',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='ScheduleStaff',
        ),
    ]

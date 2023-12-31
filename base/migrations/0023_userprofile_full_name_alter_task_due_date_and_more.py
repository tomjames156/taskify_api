# Generated by Django 4.2.3 on 2023-08-22 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_task_due_date_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 9, 23, 18, 904077, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]

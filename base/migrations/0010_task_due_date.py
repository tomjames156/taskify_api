# Generated by Django 4.2.3 on 2023-08-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_status_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 14, 9, 53, 4, 997709, tzinfo=datetime.timezone.utc)),
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-17 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_task_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='body',
            new_name='header',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 13, 31, 4, 644494, tzinfo=datetime.timezone.utc)),
        ),
    ]

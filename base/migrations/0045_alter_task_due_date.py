# Generated by Django 4.2.3 on 2023-09-12 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_alter_task_due_date_userfriending_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 13, 13, 38, 2, 954018, tzinfo=datetime.timezone.utc)),
        ),
    ]
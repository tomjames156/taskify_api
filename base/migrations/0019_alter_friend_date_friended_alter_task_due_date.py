# Generated by Django 4.2.3 on 2023-08-21 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_friend_date_friended_alter_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 8, 25, 44, 972563, tzinfo=datetime.timezone.utc)),
        ),
    ]
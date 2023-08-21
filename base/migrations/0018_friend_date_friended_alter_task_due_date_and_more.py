# Generated by Django 4.2.3 on 2023-08-21 08:24

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0017_rename_friends_friend_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='date_friended',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 21, 8, 24, 14, 696121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 8, 24, 14, 696121, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('friend_user', 'friending_user')},
        ),
    ]

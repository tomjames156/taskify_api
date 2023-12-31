# Generated by Django 4.2.3 on 2023-08-27 08:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_profilepic_user_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_pix', to='base.userprofile'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 8, 27, 22, 635532, tzinfo=datetime.timezone.utc)),
        ),
    ]

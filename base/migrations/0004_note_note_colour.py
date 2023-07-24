# Generated by Django 4.2.3 on 2023-07-21 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_note_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_colour',
            field=models.TextField(choices=[('blue', 'blue-theme'), ('green', 'green-theme'), ('orange', 'orange-theme'), ('red', 'red-theme'), ('purple', 'purple-theme')], default=datetime.datetime(2023, 7, 21, 14, 11, 4, 154823, tzinfo=datetime.timezone.utc), max_length=6),
            preserve_default=False,
        ),
    ]

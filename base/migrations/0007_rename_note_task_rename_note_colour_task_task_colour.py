# Generated by Django 4.2.3 on 2023-08-10 16:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_alter_note_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='note_colour',
            new_name='task_colour',
        ),
    ]

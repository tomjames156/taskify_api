# Generated by Django 4.2.3 on 2023-07-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_note_note_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_colour',
            field=models.TextField(choices=[('#34ccff', 'blue-theme'), ('#e4f78f', 'green-theme'), ('#ffc983', 'orange-theme'), ('#ffa0a1', 'red-theme'), ('#b99aff', 'purple-theme')], max_length=7),
        ),
    ]

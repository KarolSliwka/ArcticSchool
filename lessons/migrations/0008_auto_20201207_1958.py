# Generated by Django 3.1.2 on 2020-12-07 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20201207_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='order',
            new_name='display_order',
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-10 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_auto_20201207_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='promo_text',
        ),
    ]
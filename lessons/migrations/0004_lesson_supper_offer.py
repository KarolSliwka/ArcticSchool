# Generated by Django 3.1.2 on 2020-12-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20201214_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='supper_offer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_remove_userprofile_receiving_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='receiving_newsletter',
            field=models.CharField(blank=True, choices=[(True, 'Yes'), (False, 'No')], max_length=3),
        ),
    ]

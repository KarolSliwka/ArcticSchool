# Generated by Django 3.1.2 on 2020-12-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='about',
            field=models.TextField(max_length=500),
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0003_auto_20201216_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='open_season',
            field=models.TextField(default='December - April', max_length=120),
        ),
    ]

# Generated by Django 3.1.2 on 2020-12-07 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('lessons', '0002_auto_20201206_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.levelcard'),
        ),
    ]
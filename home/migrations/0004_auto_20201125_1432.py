# Generated by Django 3.1.2 on 2020-11-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201125_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='icon',
            field=models.CharField(choices=[('fa-facebook-f', 'Facebook'), ('fa-youtube', 'Youtube'), ('fa-pinterest-p', 'Pintereset'), ('fa-snapchat-ghost', 'Snapchat'), ('fa-twitter', 'Twitter'), ('fa-instagram', 'Instagram'), ('fa-tiktok', 'Tiktok'), ('fa-viemo-v', 'Vimeo')], max_length=30),
        ),
    ]

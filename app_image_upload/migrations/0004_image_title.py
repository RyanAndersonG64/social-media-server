# Generated by Django 5.0.6 on 2024-06-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0003_userpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(default='Pointless Default Title Because Django is Being Stupid'),
        ),
    ]
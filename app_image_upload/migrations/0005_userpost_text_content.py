# Generated by Django 5.0.6 on 2024-06-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0004_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='text_content',
            field=models.TextField(default='q'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-05 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0009_remove_userpost_post_images_image_posted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='posted_by',
        ),
    ]

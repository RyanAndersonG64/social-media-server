# Generated by Django 5.0.6 on 2024-06-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0006_remove_userpost_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='like_count',
        ),
        migrations.AddField(
            model_name='userpost',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to='app_image_upload.profile'),
        ),
    ]

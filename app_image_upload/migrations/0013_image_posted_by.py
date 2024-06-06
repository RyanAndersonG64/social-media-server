# Generated by Django 5.0.6 on 2024-06-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_image_upload', '0012_alter_userpost_text_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=models.SET('Deleted User'), to='app_image_upload.profile'),
            preserve_default=False,
        ),
    ]

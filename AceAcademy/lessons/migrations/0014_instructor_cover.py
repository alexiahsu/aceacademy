# Generated by Django 2.2.14 on 2020-08-27 00:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_auto_20200826_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='cover',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]

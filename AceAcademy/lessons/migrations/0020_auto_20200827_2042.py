# Generated by Django 2.2.14 on 2020-08-27 12:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0019_auto_20200827_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='cover',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]

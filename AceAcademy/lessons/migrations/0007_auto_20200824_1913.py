# Generated by Django 2.2.14 on 2020-08-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_lesson_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='qualifications',
            field=models.TextField(),
        ),
    ]

# Generated by Django 2.2.14 on 2020-08-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0029_auto_20200828_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField()),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
    ]
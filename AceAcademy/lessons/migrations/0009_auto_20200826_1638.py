# Generated by Django 2.2.14 on 2020-08-26 08:38

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20200826_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='SGD', max_digits=10),
        ),
    ]
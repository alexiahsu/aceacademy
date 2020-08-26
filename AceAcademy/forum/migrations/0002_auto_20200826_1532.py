# Generated by Django 2.2.14 on 2020-08-26 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateField()),
                ('comment_content', models.TextField()),
                ('comment_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_title', models.CharField(max_length=255)),
                ('thread_date', models.DateField()),
                ('thread_content', models.TextField()),
                ('thread_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='forum',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.AddField(
            model_name='comments',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]

# Generated by Django 2.2.14 on 2020-08-29 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0030_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_title', models.CharField(max_length=255)),
                ('thread_content', models.TextField()),
                ('full_name', models.CharField(max_length=255)),
                ('tags', models.CharField(choices=[('Primary Math', 'Primary Mathematics'), ('Additional Math', 'Additional Mathematics'), ('Elementary Math', 'Elementary Mathematics'), ('H1 Math', 'H1 Mathematics'), ('H2 Math', 'H2 Mathematics')], default='H2 Math', max_length=100)),
                ('education_level', models.CharField(choices=[('Lower Primary', 'Lower Primary'), ('Upper Primary', 'Upper Primary'), ('Lower Secondary', 'Lower Secondary'), ('Upper Secondary', 'Upper Secondary'), ('Junior College', 'JC')], default='Junior College', max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Public',
        ),
        migrations.AddField(
            model_name='commentforum',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Forum'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-06-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0003_remove_screen_unique_index_alter_screen_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='background_color',
            field=models.CharField(default='#fffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='screen',
            name='body_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='screen',
            name='git_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='screen',
            name='header_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='screen',
            name='is_app_screen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='screen',
            name='web_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]

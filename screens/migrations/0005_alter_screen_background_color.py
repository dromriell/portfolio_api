# Generated by Django 4.0.1 on 2022-06-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0004_screen_background_color_screen_body_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
    ]

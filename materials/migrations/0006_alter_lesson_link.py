# Generated by Django 5.0.2 on 2024-03-24 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_lesson_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.RegexValidator('\\b[A-Za-z0-9._%+-]+@yourtube+\\.com\\b')], verbose_name='ссылка на видео'),
        ),
    ]

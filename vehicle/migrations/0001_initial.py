# Generated by Django 5.0.2 on 2024-02-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='назваие')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'машина',
                'verbose_name_plural': 'машины',
            },
        ),
    ]

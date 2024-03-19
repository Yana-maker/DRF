# Generated by Django 5.0.2 on 2024-03-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='фото')),
                ('link', models.TextField(blank=True, null=True, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('lesson', models.ManyToManyField(to='materials.lesson', verbose_name='уроки')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]

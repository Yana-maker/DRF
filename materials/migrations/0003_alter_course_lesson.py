# Generated by Django 5.0.2 on 2024-03-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_course_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lesson',
            field=models.ManyToManyField(to='materials.lesson', verbose_name='уроки'),
        ),
    ]
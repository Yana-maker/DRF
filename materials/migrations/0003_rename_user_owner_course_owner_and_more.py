# Generated by Django 5.0.2 on 2024-03-19 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_user_owner_lesson_user_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='user_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='user_owner',
            new_name='owner',
        ),
    ]

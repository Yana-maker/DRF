# Generated by Django 5.0.2 on 2024-03-19 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='owner',
            new_name='user_owner',
        ),
    ]

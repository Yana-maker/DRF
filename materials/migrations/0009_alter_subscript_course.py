# Generated by Django 5.0.2 on 2024-03-26 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_alter_subscript_is_active_subscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscript',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscripts', to='materials.course', verbose_name='курс'),
        ),
    ]

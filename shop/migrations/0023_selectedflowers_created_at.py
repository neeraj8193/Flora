# Generated by Django 5.0.1 on 2024-05-03 09:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_alter_selectedflowers_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedflowers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.1 on 2024-04-19 09:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_select_flowers_selected_flowers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='selected_flowers',
            new_name='SelectedFlowers',
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-14 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_type_of_flower_pots'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='type_of_flower_pots',
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_vendorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedflowers',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_selected_flowers_selectedflowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowersoption',
            name='season_type',
            field=models.CharField(choices=[('summer', 'summer'), ('winter', 'winter'), ('spring', 'spring'), ('autumn', 'autumn'), ('All', 'All')], max_length=20),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorprofile',
            name='about',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='phone',
            field=models.CharField(max_length=18),
        ),
    ]

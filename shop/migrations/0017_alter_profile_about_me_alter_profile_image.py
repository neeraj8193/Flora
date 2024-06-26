# Generated by Django 5.0.4 on 2024-04-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_profile_about_me_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='Ashu', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='profile_image'),
        ),
    ]

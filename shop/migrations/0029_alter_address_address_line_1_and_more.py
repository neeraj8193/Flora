# Generated by Django 5.0.1 on 2024-05-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_squashed_0028_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_1',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/profile_imagedefault.png', null=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='selectedflowers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='sub_type',
            field=models.IntegerField(choices=[(0, 'monthly'), (1, 'yearly')]),
        ),
    ]

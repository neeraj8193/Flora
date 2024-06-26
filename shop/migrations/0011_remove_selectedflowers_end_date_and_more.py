# Generated by Django 5.0.1 on 2024-04-22 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_next_payment_date_subscription_expiry_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedflowers',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='selectedflowers',
            name='is_payment_done',
        ),
        migrations.RemoveField(
            model_name='selectedflowers',
            name='price',
        ),
        migrations.RemoveField(
            model_name='selectedflowers',
            name='start_date',
        ),
        migrations.AddField(
            model_name='selectedflowers',
            name='flower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.flowersoption'),
        ),
        migrations.AddField(
            model_name='selectedflowers',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subscription'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='selectedflowers',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-11 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0003_auto_20190110_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='profile_image'),
            preserve_default=False,
        ),
    ]

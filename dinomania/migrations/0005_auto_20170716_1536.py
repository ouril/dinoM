# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinomania', '0004_auto_20170714_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='test'),
        ),
    ]
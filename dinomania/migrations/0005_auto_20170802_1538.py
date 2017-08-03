# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 15:38
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinomania', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата и время'),
        ),
    ]
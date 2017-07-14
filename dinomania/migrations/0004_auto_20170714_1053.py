# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinomania', '0003_new_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя автора')),
                ('site', models.URLField(blank=True, verbose_name='Статья')),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название книги')),
                ('site', models.URLField(blank=True, verbose_name='Статья')),
                ('about', models.TextField(blank=True)),
                ('foto', models.ImageField(blank=True, upload_to='test')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dinomania.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Resurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название сайта')),
                ('site', models.URLField(blank=True, verbose_name='Статья')),
                ('about', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='dino',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dino',
            name='foto',
            field=models.ImageField(blank=True, upload_to='test'),
        ),
    ]

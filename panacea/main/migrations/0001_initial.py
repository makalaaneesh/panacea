# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main/images/large')),
                ('thumbnail', models.ImageField(blank=True, max_length=500, null=True, upload_to='main/images/thumbs')),
                ('category', models.ManyToManyField(related_name='paintings', to='main.Category')),
            ],
        ),
    ]

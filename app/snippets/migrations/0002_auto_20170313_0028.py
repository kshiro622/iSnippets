# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-13 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='snippet',
            field=models.TextField(max_length=1000),
        ),
    ]

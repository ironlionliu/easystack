# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20160826_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=10, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='wojiushialbb',
            name='password',
            field=models.CharField(max_length=10, verbose_name='password'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_truck',
            field=models.NullBooleanField(default=None),
        ),
    ]
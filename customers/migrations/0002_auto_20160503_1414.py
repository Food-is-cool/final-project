# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='profile',
        ),
        migrations.DeleteModel(
            name='CustomerProfile',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0004_remove_truckprofile_profile'),
        ('customers', '0004_remove_customerprofile_profile'),
        ('mainsite', '0004_auto_20160503_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 20:35
from __future__ import unicode_literals

from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.create(name='trucks')
    Group.objects.create(name='customers')

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]

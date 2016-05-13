# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0010_auto_20160513_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckprofile',
            name='item_10_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_1_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_2_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_3_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_4_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_5_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_6_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_7_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_8_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='item_9_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='truckprofile',
            name='menu_item_10',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

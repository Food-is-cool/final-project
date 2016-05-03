# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('want_texts', models.BooleanField(default=False)),
                ('want_emails', models.BooleanField(default=False)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=12, null=True)),
                ('street_address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('suite_number', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to='mainsite.Profile')),
            ],
        ),
    ]

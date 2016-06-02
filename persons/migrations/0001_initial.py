# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('initiated_activities', models.DateField(blank=True, null=True, verbose_name='initiated activities')),
            ],
            options={
                'verbose_name_plural': 'companies',
                'verbose_name': 'company',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='PhysicalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, default='', max_length=150, verbose_name='street address')),
                ('floor_number', models.CharField(blank=True, default='', max_length=4, verbose_name='floor number')),
                ('apartment_number', models.CharField(blank=True, default='', max_length=6, verbose_name='apartment number')),
                ('postal_code', models.CharField(blank=True, default='', max_length=20, verbose_name='postal code')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='physical_addresses', related_query_name='physical_address', to='cities_light.City', to_field='geoname_id', verbose_name='city')),
            ],
            options={
                'verbose_name_plural': 'physical addresses',
                'verbose_name': 'physical address',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]

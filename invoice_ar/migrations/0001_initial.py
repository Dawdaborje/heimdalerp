# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvoiceAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit', models.CharField(blank=True, default='', help_text="Clave Única de Identificación Tributaria means Unique Code of Tributary Identification. Everybody who isn't an employee under somebody's payroll has one. Even companies, NGOs, Fundations, etc.", max_length=14, unique=True, verbose_name='CUIT')),
                ('iibb', models.CharField(blank=True, default='', help_text="Ingresos Brutos means Brute Income. It is a unique code given by fiscal regulators of provinces'.", max_length=15, verbose_name='IIBB')),
                ('invoice_company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.CompanyInvoice', verbose_name='company')),
            ],
            options={
                'verbose_name_plural': 'companies',
                'verbose_name': 'company',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='ContactInvoiceAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(blank=True, choices=[('D', 'DNI'), ('T', 'CUIT'), ('L', 'CUIL')], max_length=1, null=True, verbose_name='id type')),
                ('id_number', models.CharField(blank=True, default='', max_length=14, verbose_name='id number')),
                ('invoice_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.ContactInvoice', verbose_name='contact')),
            ],
            options={
                'verbose_name_plural': 'contacts',
                'verbose_name': 'contact',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]

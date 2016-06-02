# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. Cambridge University', max_length=150, unique=True, verbose_name='academic institution')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'academic institution',
                'verbose_name_plural': 'academic institutions',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='A single-time achievement; i.e. Jessica finished her project 3 months earlier', verbose_name='description')),
                ('when_it_happened', models.DateField(blank=True, help_text='Not necessarily the current date.', null=True, verbose_name='when it happened')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'achievement',
                'verbose_name_plural': 'achievements',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('description', models.CharField(default='', max_length=150, verbose_name='description')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'aptitude',
                'verbose_name_plural': 'aptitudes',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', related_query_name='area', to='persons.Company', verbose_name='company')),
            ],
        ),
        migrations.CreateModel(
            name='AreaHasEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_since', models.DateField(blank=True, null=True, verbose_name='date since')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Area', verbose_name='area')),
            ],
            options={
                'verbose_name': 'company has employee',
                'verbose_name_plural': 'company has employees',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. Lawyer, Accountant, Civil Engineer', max_length=30, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'degree',
                'verbose_name_plural': 'degrees',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('phone_numbers', models.CharField(blank=True, default='', max_length=300, verbose_name='phone numbers')),
                ('extra_emails', models.CharField(blank=True, default='', max_length=300, verbose_name='extra email addresses')),
                ('genre', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='genre')),
                ('achievements', models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', to='hr.Achievement', verbose_name='achievements')),
                ('aptitudes', models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', to='hr.Aptitude', verbose_name='aptitudes')),
                ('areas', models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', through='hr.AreaHasEmployee', to='hr.Area', verbose_name='areas')),
                ('born_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country', to_field='geoname_id', verbose_name='born in')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='EmployeeHasDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingress_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='ingress year')),
                ('egress_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='egress year')),
                ('academic_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.AcademicInstitution', verbose_name='academic institution')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Degree', verbose_name='degree')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'employee has degree',
                'verbose_name_plural': 'employees have degrees',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='EmployeeHasRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_since', models.DateField(blank=True, null=True, verbose_name='date since')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'employee has role',
                'verbose_name_plural': 'employee has roles',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='EmployeeHasSanction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_happened', models.TextField(default='', verbose_name='what happened')),
                ('when_it_happened', models.DateTimeField(help_text='Not necessarily the current date', verbose_name='when it happened')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Employee', verbose_name='employee')),
                ('others_implicated', models.ManyToManyField(blank=True, related_name='implicated_in_sanctions', related_query_name='implicated_in_sanction', to='hr.Employee', verbose_name='others implicated')),
            ],
            options={
                'verbose_name': 'employee has degree',
                'verbose_name_plural': 'employees have degrees',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='EmployeeSpeaksLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('B', 'Basic'), ('M', 'Medium'), ('A', 'Advanced'), ('N', 'Native')], default='', max_length=1, verbose_name='level')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, help_text='Points should be proportional to the level spoken.', max_digits=5, verbose_name='points')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'employee speaks language',
                'verbose_name_plural': 'employee speaks languages',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. Italic, Hispanic, Black, Arabic, White, Latin', max_length=30, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'ethnicity',
                'verbose_name_plural': 'ethnicities',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='Sanction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('description', models.CharField(default='', help_text='A brief explanation of what consists of.', max_length=250, verbose_name='description')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, help_text="Enter points greater than zero here, but they'll be sustracted rather than added from the total.", max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'sanction type',
                'verbose_name_plural': 'sanction types',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='SexualOrientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='i.e. Straight, Homosexual, Pansexual, Transexual', max_length=30, unique=True, verbose_name='name')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='points')),
            ],
            options={
                'verbose_name': 'sexual orientation',
                'verbose_name_plural': 'sexual orientations',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.AddField(
            model_name='employeespeakslanguage',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Language', verbose_name='language'),
        ),
        migrations.AddField(
            model_name='employeehassanction',
            name='sanction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Sanction', verbose_name='sanction'),
        ),
        migrations.AddField(
            model_name='employeehassanction',
            name='victims',
            field=models.ManyToManyField(blank=True, related_name='sanction_victims', related_query_name='sanction_victim', to='hr.Employee', verbose_name='victims'),
        ),
        migrations.AddField(
            model_name='employeehasrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Role', verbose_name='roles'),
        ),
        migrations.AddField(
            model_name='employee',
            name='degree',
            field=models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', through='hr.EmployeeHasDegree', to='hr.Degree', verbose_name='degrees'),
        ),
        migrations.AddField(
            model_name='employee',
            name='ethnicities',
            field=models.ManyToManyField(blank=True, help_text='Relevant for countries where one must comply quotas', related_name='employees', related_query_name='employee', to='hr.Ethnicity', verbose_name='ethnicities'),
        ),
        migrations.AddField(
            model_name='employee',
            name='home_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='persons.PhysicalAddress', verbose_name='home address'),
        ),
        migrations.AddField(
            model_name='employee',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', through='hr.EmployeeSpeaksLanguage', to='hr.Language', verbose_name='languages'),
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', through='hr.EmployeeHasRole', to='hr.Role', verbose_name='roles'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sanctions',
            field=models.ManyToManyField(blank=True, related_name='employees', related_query_name='employee', through='hr.EmployeeHasSanction', to='hr.Sanction', verbose_name='sanctions'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sexual_orientation',
            field=models.ForeignKey(blank=True, help_text='Relevant for countries where one must comply quotas', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', related_query_name='employee', to='hr.SexualOrientation', verbose_name='sexual orientation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='areahasemployee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='hr.Employee', verbose_name='employee'),
        ),
        migrations.AlterUniqueTogether(
            name='areahasemployee',
            unique_together=set([('area', 'employee')]),
        ),
    ]

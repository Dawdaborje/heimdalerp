# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(max_length=30, verbose_name='code')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('account_type', models.CharField(blank=True, choices=[('P', 'Personal'), ('R', 'Real'), ('N', 'Nominal')], max_length=1, null=True, verbose_name='main type')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='balance')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'accounts',
                'verbose_name': 'account',
            },
        ),
        migrations.CreateModel(
            name='CompanyAccounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_credit_account_for_applepay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for Apple Pay')),
                ('default_credit_account_for_bankaccount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for bank account')),
                ('default_credit_account_for_bitcoin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for Bitcoin')),
                ('default_credit_account_for_cash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for cash')),
                ('default_credit_account_for_check', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for check')),
                ('default_credit_account_for_creditcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for credit card')),
                ('default_credit_account_for_debitcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for debit card')),
                ('default_credit_account_for_googlewallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for Google Wallet')),
                ('default_credit_account_for_paypal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default credit account for PayPal')),
                ('default_debit_account_for_applepay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for Apple Pay')),
                ('default_debit_account_for_bankaccount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for bank account')),
                ('default_debit_account_for_bitcoin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for Bitcoin')),
                ('default_debit_account_for_cash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for cash')),
                ('default_debit_account_for_check', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for check')),
                ('default_debit_account_for_creditcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for credit card')),
                ('default_debit_account_for_debitcard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for debit card')),
                ('default_debit_account_for_googlewallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for Google Wallet')),
                ('default_debit_account_for_paypal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Account', verbose_name='default debit account for PayPal')),
                ('persons_company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.Company', verbose_name='company')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'companies',
                'verbose_name': 'company',
            },
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('persons_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ledgers', related_query_name='ledger', to='persons.Company', verbose_name='company')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'ledgers',
                'verbose_name': 'ledger',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(help_text='Not necessarily today.', verbose_name='payment date')),
                ('payment_type', models.CharField(choices=[('S', 'Send'), ('R', 'Receive'), ('I', 'Internal')], default='R', max_length=1, verbose_name='payment type')),
                ('payment_method', models.CharField(choices=[('C', 'Cash'), ('CC', 'Credit Card'), ('DB', 'Debit Card'), ('B', 'Bank Account'), ('CH', 'Check'), ('P', 'PayPal'), ('GW', 'Google Wallet'), ('AP', 'Apple Pay'), ('BC', 'Bitcoin')], default='C', max_length=2, verbose_name='payment method')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='amount')),
                ('accounting_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', related_query_name='payment', to='accounting.CompanyAccounting', verbose_name='company')),
                ('contact_contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', related_query_name='payment', to='contact.Contact', verbose_name='contact')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'payments',
                'verbose_name': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='amount')),
                ('debit_account_balance', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='account balance')),
                ('credit_account_balance', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='credit account balance')),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_transactions', related_query_name='credit_transaction', to='accounting.Account', verbose_name='credit account')),
                ('debit_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debit_transactions', related_query_name='debit_transaction', to='accounting.Account', verbose_name='debit account')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'transactions',
                'verbose_name': 'transaction',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='+', to='accounting.Transaction', verbose_name='transaction'),
        ),
        migrations.AddField(
            model_name='account',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accounts', related_query_name='account', to='accounting.Ledger', verbose_name='ledger'),
        ),
        migrations.AlterUniqueTogether(
            name='ledger',
            unique_together=set([('persons_company', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('ledger', 'code')]),
        ),
    ]

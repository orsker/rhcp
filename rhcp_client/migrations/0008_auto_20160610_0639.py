# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 06:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhcp_client', '0007_auto_20160610_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_site_tariff',
            name='client',
        ),
        migrations.RemoveField(
            model_name='client_site_tariff',
            name='tariff',
        ),
        migrations.DeleteModel(
            name='client_site_tariff',
        ),
    ]

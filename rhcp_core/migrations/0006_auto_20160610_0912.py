# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhcp_core', '0005_remove_site_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain_tariff',
            old_name='date_inactive',
            new_name='date_stop',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='date_resume',
            new_name='date_stop',
        ),
        migrations.RenameField(
            model_name='site_tariff',
            old_name='date_inactive',
            new_name='date_stop',
        ),
    ]

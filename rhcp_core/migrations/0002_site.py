# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-10 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rhcp_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u0418\u043c\u044f')),
                ('active', models.BooleanField(default=False, verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('date_resume', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438')),
                ('site_tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rhcp_core.site_tariff')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'rhcp_site',
                'verbose_name': '\u0421\u0430\u0439\u0442',
                'verbose_name_plural': '\u0421\u0430\u0439\u0442\u044b',
            },
        ),
    ]
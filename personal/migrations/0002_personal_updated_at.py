# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 02:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 24, 2, 4, 9, 619409, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

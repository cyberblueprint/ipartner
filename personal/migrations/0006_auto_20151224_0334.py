# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20151224_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='products',
        ),
        migrations.AddField(
            model_name='producto',
            name='products',
            field=models.ManyToManyField(choices=[('infraestructura', 'infraestructura'), ('software', 'software'), ('kpi', 'kpi'), ('contratos', 'contratos')], related_name='products', to='personal.Empresa'),
        ),
    ]

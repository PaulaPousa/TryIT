# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        ('editions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.Attendant'),
        ),
    ]

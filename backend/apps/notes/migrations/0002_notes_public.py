# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-26 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]

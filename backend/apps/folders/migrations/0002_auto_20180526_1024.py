# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-26 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='folder',
            options={'verbose_name': 'Folder', 'verbose_name_plural': 'Folders'},
        ),
    ]

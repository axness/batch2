# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-06 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180601_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='publisher_url',
            new_name='url',
        ),
    ]

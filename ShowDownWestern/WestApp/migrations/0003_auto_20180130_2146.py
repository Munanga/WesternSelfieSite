# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WestApp', '0002_auto_20180130_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='image_thumbnail',
            new_name='image',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 03:43
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WestApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='media'),
        ),
    ]

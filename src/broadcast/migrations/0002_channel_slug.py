# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=140, unique=True),
            preserve_default=False,
        ),
    ]

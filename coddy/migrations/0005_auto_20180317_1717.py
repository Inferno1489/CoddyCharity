# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-17 14:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coddy', '0004_auto_20180317_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 3, 17, 17, 17, 25, 689662)),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2018, 3, 17, 17, 17, 25, 690623)),
        ),
    ]

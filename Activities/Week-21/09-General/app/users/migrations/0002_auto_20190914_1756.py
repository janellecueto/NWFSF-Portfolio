# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-09-14 17:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 17, 56, 17, 645841, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 17, 56, 17, 646185, tzinfo=utc)),
        ),
    ]

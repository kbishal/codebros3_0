# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 21:53
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 21, 53, 54, 680644, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

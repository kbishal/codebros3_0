# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-02 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review_it', '0003_auto_20161002_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
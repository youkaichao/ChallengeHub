# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_auto_20181120_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
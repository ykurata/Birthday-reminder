# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 20:25
from __future__ import unicode_literals

from django.db import migrations
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0005_auto_20190711_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='date_of_birth',
            field=djangoyearlessdate.models.YearlessDateField(max_length=4, null=True),
        ),
    ]

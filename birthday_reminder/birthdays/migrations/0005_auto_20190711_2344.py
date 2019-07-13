# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0004_auto_20190711_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birthday',
            name='day',
        ),
        migrations.RemoveField(
            model_name='birthday',
            name='month',
        ),
        migrations.AddField(
            model_name='birthday',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
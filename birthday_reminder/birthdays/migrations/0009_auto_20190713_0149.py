# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-13 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0008_auto_20190713_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]

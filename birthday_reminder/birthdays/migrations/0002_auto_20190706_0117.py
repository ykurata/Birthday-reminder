# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-06 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='January', max_length=100),
        ),
    ]
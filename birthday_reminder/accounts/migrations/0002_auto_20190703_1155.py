# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-03 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usernmae',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='avator',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
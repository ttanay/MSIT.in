# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-11 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170311_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentpage',
            name='order',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='tab',
            name='order',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-20 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import functools
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_merge_20170319_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='department',
            field=models.CharField(blank=True, choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('APPLIED SCIENCES', 'Applied Sciences')], help_text='Department Name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='lecture_plan',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(web.models.wrapper, *(), **{b'field': 'title', b'folder': 'lecture_plan'})),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(web.models.wrapper, *(), **{b'field': 'title', b'folder': 'syllabus'})),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskstatus',
            field=models.IntegerField(default=0),
        ),
    ]

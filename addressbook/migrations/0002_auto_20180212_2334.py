# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='company',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='manager',
            field=models.CharField(default='Adam', max_length=200),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]

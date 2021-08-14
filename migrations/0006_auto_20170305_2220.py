# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20170305_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='thesis_title',
            field=models.CharField(blank=True, help_text='Title of Thesis or Dissertation, etc', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='thesis_type',
            field=models.CharField(blank=True, help_text='e.g. Thesis, Dissertation, etc', max_length=50, null=True),
        ),
    ]

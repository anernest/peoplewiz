# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('major', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisor', to='people.Person')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_department', to='people.Organization')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='people.Organization')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='people.Person')),
            ],
        ),
    ]

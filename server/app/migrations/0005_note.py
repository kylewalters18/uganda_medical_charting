# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-28 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170122_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=b'2017-01-28T09:32:00')),
                ('note', models.CharField(max_length=2000)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='app.Patient')),
            ],
        ),
    ]
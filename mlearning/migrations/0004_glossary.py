# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlearning', '0003_auto_20161123_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]

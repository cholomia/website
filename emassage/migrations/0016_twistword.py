# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emassage', '0015_grade_try_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwistWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('clue', models.TextField()),
            ],
        ),
    ]

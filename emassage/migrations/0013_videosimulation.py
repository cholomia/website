# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emassage', '0012_auto_20170116_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSimulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]

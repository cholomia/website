# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlearning', '0006_auto_20170217_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='lesson_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessment_lesson_detail', to='mlearning.LessonDetail'),
        ),
    ]

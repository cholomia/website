# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emassage', '0006_auto_20161222_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_score', models.IntegerField()),
                ('item_count', models.IntegerField()),
                ('lesson', models.ForeignKey(related_name='grades', to='emassage.Lesson')),
                ('user', models.ForeignKey(related_name='user_grades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ('-created',)},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0006_course_manager_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 21, 48, 31, 137000)),
        ),
        migrations.AddField(
            model_name='homework',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 21, 48, 31, 137000)),
        ),
        migrations.AddField(
            model_name='homeworkfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 21, 48, 31, 138000)),
        ),
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 21, 48, 31, 139000)),
        ),
        migrations.AddField(
            model_name='resource',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 21, 48, 31, 138000)),
        ),
        migrations.AddField(
            model_name='resource',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
    ]

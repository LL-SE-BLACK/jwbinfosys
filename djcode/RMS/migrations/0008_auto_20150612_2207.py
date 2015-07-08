# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0007_auto_20150612_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 7, 48, 193000)),
        ),
        migrations.AlterField(
            model_name='homework',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 7, 48, 193000)),
        ),
        migrations.AlterField(
            model_name='homeworkfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 7, 48, 193000)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 7, 48, 195000)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 22, 7, 48, 195000)),
        ),
    ]

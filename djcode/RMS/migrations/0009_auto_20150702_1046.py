# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0008_auto_20150612_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.CharField(default=b'1', max_length=8)),
                ('homework_num', models.CharField(default=b'1', max_length=8)),
                ('is_view', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='homework',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 46, 51, 912000)),
        ),
        migrations.AlterField(
            model_name='homework',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 46, 51, 912000)),
        ),
        migrations.AlterField(
            model_name='homeworkfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 46, 51, 914000)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 46, 51, 918000)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 46, 51, 916000)),
        ),
    ]

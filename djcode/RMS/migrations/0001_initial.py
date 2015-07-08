# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('student_id', models.CharField(max_length=8)),
                ('course_id', models.CharField(max_length=8)),
                ('teacher_id', models.CharField(max_length=8)),
                ('manager_id', models.CharField(max_length=8)),
            ],
        ),
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
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('homework_num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('course_id', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2015, 7, 8, 10, 35, 25, 185085))),
                ('end_date', models.DateTimeField(default=datetime.datetime(2015, 7, 8, 10, 35, 25, 185118))),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkFile',
            fields=[
                ('homework_id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('homework_num', models.CharField(max_length=8)),
                ('course_id', models.CharField(max_length=8)),
                ('student_id', models.CharField(max_length=8)),
                ('homework_add', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 7, 8, 10, 35, 25, 185837))),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('notice_title', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=8)),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 7, 8, 10, 35, 25, 187266))),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('course_id', models.CharField(max_length=8)),
                ('resource_name', models.CharField(max_length=20)),
                ('resource_add', models.CharField(max_length=100)),
                ('resource_top', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 7, 8, 10, 35, 25, 186532))),
                ('frequency', models.IntegerField(default=0)),
            ],
        ),
    ]

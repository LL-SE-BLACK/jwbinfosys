# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('homework_num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('course_id', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=100)),
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
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('course_id', models.CharField(max_length=8)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('course_id', models.CharField(max_length=8)),
                ('resource_name', models.CharField(max_length=20)),
                ('resource_add', models.CharField(max_length=100)),
            ],
        ),
    ]

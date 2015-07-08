# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0017_auto_20150707_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_info',
            name='id',
        ),
        migrations.AddField(
            model_name='class_info',
            name='examdate',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='class_table',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='course_info',
            name='introduce',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='faculty_user',
            name='introduce',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='class_id',
            field=models.CharField(serialize=False, primary_key=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='course_id',
            field=models.ForeignKey(to='IMS.Course_info', related_name='class_course'),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='examroom',
            field=models.CharField(default='00000000000000000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='examtime',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='teacher',
            field=models.ForeignKey(to='IMS.Faculty_user'),
        ),
        migrations.AlterField(
            model_name='class_info',
            name='time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='class_table',
            name='id',
            field=models.CharField(serialize=False, primary_key=True, max_length=10),
        ),
    ]

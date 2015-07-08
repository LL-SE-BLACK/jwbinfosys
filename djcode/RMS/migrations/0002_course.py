# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('num', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('student_id', models.CharField(max_length=8)),
                ('course_id', models.CharField(max_length=8)),
            ],
        ),
    ]

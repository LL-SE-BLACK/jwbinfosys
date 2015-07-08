# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0005_course_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='manager_id',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]

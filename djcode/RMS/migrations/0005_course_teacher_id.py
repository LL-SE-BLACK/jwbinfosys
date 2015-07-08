# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0004_resource_resource_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]

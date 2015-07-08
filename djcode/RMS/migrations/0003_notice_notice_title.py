# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='notice_title',
            field=models.CharField(default=111, max_length=100),
            preserve_default=False,
        ),
    ]

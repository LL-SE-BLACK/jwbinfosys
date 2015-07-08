# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0003_notice_notice_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource_top',
            field=models.CharField(default='top', max_length=20),
            preserve_default=False,
        ),
    ]

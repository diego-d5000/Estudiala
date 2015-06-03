# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20150527_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='r_type',
        ),
    ]

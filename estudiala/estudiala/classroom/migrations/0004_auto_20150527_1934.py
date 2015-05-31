# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20150527_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

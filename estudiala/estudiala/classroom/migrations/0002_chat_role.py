# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='role',
            field=models.CharField(default='estudiante', max_length=15),
            preserve_default=False,
        ),
    ]

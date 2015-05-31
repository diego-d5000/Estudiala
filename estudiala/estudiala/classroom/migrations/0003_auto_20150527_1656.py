# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_chat_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_typ', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='r_type',
            field=models.ForeignKey(default=None, to='classroom.Room_type'),
            preserve_default=False,
        ),
    ]

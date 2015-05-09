# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_auto_20150509_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo',
            old_name='tipo_usuario',
            new_name='us_tip',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_name',
        ),
        migrations.AddField(
            model_name='usuario',
            name='description',
            field=models.TextField(default=1, max_length=225, verbose_name='Descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

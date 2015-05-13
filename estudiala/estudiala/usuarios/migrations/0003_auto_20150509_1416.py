# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150508_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_usuario', models.CharField(max_length=225, verbose_name='Tipo de Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_type',
            field=models.ForeignKey(to='usuarios.Tipo'),
        ),
    ]

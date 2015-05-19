# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225, verbose_name='Nombre')),
                ('subject', models.CharField(max_length=225, verbose_name='Materia')),
                ('to_email', models.CharField(max_length=225, verbose_name='Correo del Profesor')),
                ('homework_doc', models.FileField(upload_to=b'', verbose_name='Documento de Tarea')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

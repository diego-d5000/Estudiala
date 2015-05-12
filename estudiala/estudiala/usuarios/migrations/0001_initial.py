# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=225, verbose_name='Nombre')),
                ('middle_name', models.CharField(max_length=225, verbose_name='Apellido Paterno')),
                ('last_name', models.CharField(max_length=225, null=True, verbose_name='Apellido Materno', blank=True)),
                ('email', models.EmailField(unique=True, max_length=225, verbose_name='Correo')),
                ('user_name', models.CharField(unique=True, max_length=225, verbose_name='Nombre de Usuario')),
                ('password', models.CharField(max_length=225, verbose_name='Contrasenia')),
                ('user_type', models.CharField(max_length=225, verbose_name='Tipo de Usuario')),
            ],
        ),
    ]

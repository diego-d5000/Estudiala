from django.db import models

#class Tipo(object):
#	tipo_usuario = models.CharField(max_length=225, verbose_name=u'Tipo de Usuario')

#	def __unicode__(self):
#		return self.nombre


class Usuario(models.Model):
	name = models.CharField(max_length=225,verbose_name=u'Nombre')
	middle_name = models.CharField(max_length=225, verbose_name=u'Apellido Paterno')
	last_name = models.CharField(max_length=225, blank=True, null=True, verbose_name=u'Apellido Materno')
	email = models.EmailField(max_length=225, verbose_name=u'Correo', unique=True)
	user_name = models.CharField(max_length=225, verbose_name=u'Nombre de Usuario', unique=True)
	password = models.CharField(max_length=225, verbose_name=u'Contrasenia')
	user_type = models.CharField(max_length=225, verbose_name=u'Tipo de Usuario')
	#tipo = models.ForeignKey(Tipo)

	def __unicode__(self):
		return self.nombre + '' + self.paterno


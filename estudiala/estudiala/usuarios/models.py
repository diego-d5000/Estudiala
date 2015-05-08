from django.db import models

#class Tipo(object):
#	tipo_usuario = models.CharField(max_length=225, verbose_name=u'Tipo de Usuario')

#	def __unicode__(self):
#		return self.nombre


class Usuarios(object):
	nombre = models.CharField(max_length=225,verbose_name=u'Nombre')
	paterno = models.CharField(max_length=225, verbose_name=u'Apellido Paterno')
	materno = models.CharField(max_length=225, blank=True, null=True, verbose_name=u'Apellido Materno')
	correo = models.EmailField(max_length=225, verbose_name=u'Correo', unique=True)
	nombre_usuario = models.CharField(max_length=225, verbose_name=u'Nombre de Usuario', unique=True)
	contra = models.CharField(max_length=225, verbose_name=u'Contrasenia')
	tipo = models.CharField(max_length=225, verbose_name=u'Tipo de Usuario')
	#tipo = models.ForeignKey(Tipo)

	def __unicode__(self):
		return self.nombre + '' + self.paterno


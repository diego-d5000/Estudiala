from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
	name = models.CharField(max_length=225, verbose_name=u'Nombre')
	subject = models.CharField(max_length=225, verbose_name=u'Materia')
	to_email = models.CharField(max_length=225, verbose_name=u'Correo del Profesor')
	homework_doc = models.FileField(verbose_name=u'Documento de Tarea')
	user = models.ForeignKey(User)

	def __unicode__(self):
		return 'Tarea de: '+ self.subject
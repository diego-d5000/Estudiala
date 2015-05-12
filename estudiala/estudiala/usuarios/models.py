from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
	us_tip = models.CharField(max_length=225, verbose_name=u'Tipo de Usuario')

	def __unicode__(self):
		return self.us_tip


class Usuario(models.Model):
	description = models.TextField(max_length=225, verbose_name=u'Descripcion')
	user_type = models.ForeignKey(Tipo)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.description


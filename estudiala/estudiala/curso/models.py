from django.db import models

# Create your models here.

class Curso(models.Model):

	#name; Course's name, it will be displayed in the template
	name = models.CharField(max_length=225,verbose_name=u'Name')
	
	#area; Course's study field
	area = models.CharField(max_length=225, verbose_name=u'Area')

	#Ranking; User's rating about how good/bad is the course, 0 to 10 scale
	ranking = models.IntegerField(max_length=225, verbose_name=u'Ranking')

	#Description: What the course is going to be
	description = models.CharField(max_length=255, verbose_name=u'Description')

	#Video; the video that belongs to the course
	video = models.CharField(max_length=255, verbose_name=u'Video')

	#Image; Image thumbnail of the course
	image = models.CharField(max_length=512, verbose_name=u'Image')

	#Id; Foreign key, It references the mentor of the course
	idF = models.ForeignKey(Usuario)

	def __unicode__(self):
		return self.nombre + '' + self.area
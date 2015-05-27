from django.db import models
class Room_type(models.Model):
	room_typ = models.CharField(max_length=225)

	def __unicode__(self):
		return self.room_typ

class Room(models.Model):
	name = models.CharField(max_length=128)
	n = models.CharField(max_length=16)
	r_type = models.ForeignKey(Room_type)

	def __unicode__(self):
		return self.name

class Chat(models.Model):
	username = models.CharField(max_length=64)
	role = models.CharField(max_length=15)
	text = models.CharField(max_length=280)
	date = models.CharField(max_length=35)
	room = models.ForeignKey(Room)

	def __unicode__(self):
		return self.username

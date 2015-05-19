from django import forms
from .models import Tarea
from django.contrib.auth.models import User

#Send email (Homework)
class NewEmail(forms.ModelForm):
	def save(self,user,*args,**kwargs):
		self.instance.user=user
		super(NewEmail,self).save(*args,**kwargs)

	class Meta:
		model = Tarea
		exclude = ('user',)
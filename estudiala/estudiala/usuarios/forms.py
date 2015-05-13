from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Usuario


#Signup Form
class NewUserCreationForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()

	#validar que el email no exista

	class Meta:
		model = User
		fields = ('username','email', 'first_name', 'last_name')

#	def clean_email():

#Information Form
class UserInformationForm(forms.ModelForm):

	def save(self,user,*args,**kwargs):
		self.instance.user=user
		super(UserInformationForm,self).save(*args, **kwargs)

	class Meta:
		model = Usuario
		exclude = ('user',)
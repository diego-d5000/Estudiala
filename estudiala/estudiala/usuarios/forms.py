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
		widgets = {
			'username': forms.TextInput(
				attrs={'class': 'input_field input_field-social',
				'placeholder': 'Ingresa tu usuario'}
			),
			'email': forms.TextInput(
				attrs={'class': 'input_field input_field-social',
				'placeholder': 'Ingresa tu correo'}
			),
			'first_name': forms.TextInput(
				attrs={'class': 'input_field input_field-social',
				'placeholder': 'Ingresa tu nombre'}
			),
			'last_name': forms.TextInput(
				attrs={'class': 'input_field input_field-social',
				'placeholder': 'Ingresa tu apellido'}
			),
		}


#	def clean_email():

#Information Form
class UserInformationForm(forms.ModelForm):

	def save(self,user,*args,**kwargs):
		self.instance.user=user
		super(UserInformationForm,self).save(*args, **kwargs)

	class Meta:
		model = Usuario
		exclude = ('user',)

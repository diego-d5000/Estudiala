from django import forms

#Send email (Homework)
class NewEmail(forms.Form):

	name = forms.CharField(label='Nombre')
	subject = forms.CharField(label='Materia')
	to_email = forms.EmailField(label='Correo del Profesor')
	homework_doc = forms.FileField(label='Archivo de tarea')

	class Meta:
		
		fields = ('name', 'subject', 'to_email', 'homework_doc')
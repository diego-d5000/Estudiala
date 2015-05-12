from django import forms

#Send email (Homework)
class NewEmail(forms.Form):

	subject = forms.CharField(label='Asunto')
	message = forms.CharField(label='Materia')
	to_email = forms.EmailField(label='Correo del Profesor')
	homework_doc = forms.FileField(label='Archivo de tarea')

	class Meta:
		
		fields = ('subject', 'message', 'from_email', 'to_email')
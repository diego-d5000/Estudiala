from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import NewEmail
from .models import Tarea

class homework(View):
	template_name = 'homework.html'

	def get(self,request):
		form = NewEmail()
		return render(request,self.template_name,locals())

	def post(self,request):
		form = NewEmail(request.POST, request.FILES)
		user = request.user
		email = user.email
		if form.is_valid():
			form.save(user=user)
			subject = "Tarea de: " + request.POST['subject']
			name = request.POST['name']
			user_email = email
			to_email = request.POST['to_email']
			to_list = [to_email, user_email]
			homework_doc = request.FILES['homerwork_doc']
			try:
				mail = EmailMessage(subject,name,settings.EMAIL_HOST_USER, to_list)
				mail.attach(homework_doc.name, homework_doc.read(), homework_doc.content_type)
				mail.send()
				return redirect('homework_success')
			except:
				return redirect('homework_error')
		else:
			return render(request, self.template_name, locals())

class homework_success(TemplateView):
	template_name = 'homework_success.html'

class homework_error(TemplateView):
	template_name = 'homework_error.html'

#def get_homework(request):
#	user = request.user
#	homeworks = Tarea.objects.filter(user=user)
#	print homeworks
#	return render(
#		request,
#		'homework.html',
#		{'homeworks':homeworks}
#	)

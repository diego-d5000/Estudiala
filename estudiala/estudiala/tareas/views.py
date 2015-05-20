from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import NewEmail
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class homework(View):
	template_name = 'homework.html'

	@method_decorator(login_required)
	def get(self,request):
		form = NewEmail()
		return render(request,self.template_name,locals())

	@method_decorator(login_required)
	def post(self,request):
		form = NewEmail(request.POST, request.FILES)
		user = request.user
		email = user.email
		if form.is_valid():
			subject = "Tarea de: " + request.POST['subject']
			name = request.POST['name']
			user_email = email
			to_email = request.POST['to_email']
			to_list = [to_email, user_email]
			homework_doc = request.FILES['homework_doc']
			try:
				mail = EmailMessage(subject,name,settings.EMAIL_HOST_USER, to_list)
				mail.attach(homework_doc.name, homework_doc.read(), homework_doc.content_type)
				mail.send()
				return redirect('homework_success')
			except:
				return redirect('homework_error')
		else:
			return render(request, self.template_name, locals())

@login_required(login_url='signin')
def homework_success(request):
	return render(
		request,
		'homework_success.html',
		{}
	)

@login_required(login_url='signin')
def homework_error(request):
	return render(
		request,
		'homework_error.html',
		{}
	)
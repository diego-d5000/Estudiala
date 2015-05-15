from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import NewEmail
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def homework(request):
	user = request.user
	email = user.email
	form = NewEmail(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			subject = "Tarea de: " + request.POST['subject']
			message = request.POST['message']
			user_email = email
			to_email = request.POST['to_email']
			to_list = [to_email, user_email]
			homework_doc = request.FILES['homework_doc']
			try:
				mail = EmailMessage(subject,message,settings.EMAIL_HOST_USER, to_list)
				mail.attach(homework_doc.name, homework_doc.read(), homework_doc.content_type)
				mail.send()
				return redirect('homework_success')
			except:
				return redirect('homework_error')

	return render(request, 'homework.html', {'form': form})

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
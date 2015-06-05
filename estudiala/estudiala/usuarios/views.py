from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .forms import NewUserCreationForm, UserInformationForm, ContactForm
from django.conf import settings

class signup(View):
	template_name = 'signup.html'

	def get(self,request):
		form = NewUserCreationForm()
		return render(request, self.template_name, locals())

	def post(self, request):
		form = NewUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			access = authenticate(username=username, password=password)
			if access is not None and access.is_active:
				login(request,access)
				user = request.user
				try:
					user_object = Usuario.objects.get(user=user.id)
					descript = user_object.description
				except:
					user_object=None
					descript = user_object
				if descript is None:
					return redirect('information')
				else:
					return redirect('home')
			else:
				return redirect('nouser')
		else:
			return render(request, self.template_name, locals())

class signin(View):
	template_name='signin.html'

	def get(self,request):
		form = AuthenticationForm()
		return render(request, self.template_name, locals())

	def post(self, request):
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			access = authenticate(username=username, password=password)
			if access is not None and access.is_active:
				login(request,access)
				user = request.user
				try:
					user_object = Usuario.objects.get(user=user.id)
					descript = user_object.description
				except:
					user_object=None
					descript = user_object
				if descript is None:
					return redirect('home')
			else:
				return redirect('nouser')
		else:
			return render(request, self.template_name, locals())

class information(View):
	template_name = 'info.html'

	def get(self,request):
		form = UserInformationForm()
		return render(request, self.template_name, locals())

	def post(self,request):
		form = UserInformationForm(request.POST)
		user = request.user
		if form.is_valid():
			form.save(user = user)
			return redirect('home')
		else:
			return render(request, self.template_name, locals())

class contact(View):
	template_name = 'contact.html'

	def get(self,request):
		form = ContactForm()
		return render(request, self.template_name, locals())

	def post(self,request):
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = request.POST['subject']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			message = first_name + " " + last_name + " " + request.POST['message']
			sender = request.POST['sender']
			print message
			try:
				mail = EmailMessage(subject, message, sender, settings.EMAIL_HOST_USER)
				mail.send()
				return redirect('home')
			except:
				return redirect('homework_error')
		else:
			return render(request, self.template_name, locals())

class home(TemplateView):
	template_name = 'index.html'

class user_profile(TemplateView):
	template_name = 'perfil.html'

class no_user(TemplateView):
	template_name = 'nouser.html'

class courses(TemplateView):
	template_name = 'cursos.html'

@login_required(login_url='signin')
def close(request):
	logout(request)
	return redirect('home')

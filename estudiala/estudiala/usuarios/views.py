from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from .forms import NewUserCreationForm, UserInformationForm

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
					return redirect('information')
				else:
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

class home(TemplateView):
	template_name = 'index.html'

class math_course(TemplateView):
	template_name = 'cursos/matematicas.html'

class programming_course(TemplateView):
	template_name = 'cursos/programacion.html'

class kitchen_course(TemplateView):
	template_name = 'cursos/cocina.html'

class user_profile(TemplateView):
	template_name = 'perfil.html'

class no_user(TemplateView):
	template_name = 'nouser.html'

@login_required(login_url='signin')
def close(request):
	logout(request)
	return redirect('signin')
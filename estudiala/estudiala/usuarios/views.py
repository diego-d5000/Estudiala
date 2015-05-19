from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import NewUserCreationForm, UserInformationForm
from django.utils.decorators import method_decorator

class signup(View):
	#loguear al usuario directamente
	#redireccionar a information
	template_name = 'signup.html'

	def get(self,request):
		form = NewUserCreationForm()
		return render(request, self.template_name, locals())

	def post(self,request):
		form = NewUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('information')
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
				return redirect('nouser.html')
		else:
			return render(request, self.template_name, locals())

#@login_required(login_url='signin')
class information(View):
	template_name = 'info.html'

	@method_decorator(login_required)
	def get(self,request):
		form = UserInformationForm()
		return render(request, self.template_name, locals())

	@method_decorator(login_required)
	def post(self,request):
		form = UserInformationForm(request.POST)
		user = request.user
		if form.is_valid():
			form.save(user = user)
			return redirect('home')
		else:
			return render(request, self.template_name, locals())

@login_required(login_url='signin')
def close(request):
	logout(request)
	return redirect('signin')

def home(request):
    return render(
        request,
        'index.html',
        {}
    )

def math_course(request):
	return render(
		request,
		'cursos/matematicas.html',
		{}
	)

def programming_course(request):
	return render(
		request,
		'cursos/programacion.html',
		{}
	)

def kitchen_course(request):
	return render(
		request,
		'cursos/cocina.html',
		{}
	)

@login_required(login_url='signin')
def user_profile(request):
	return render(
		request,
		'perfil.html',
		{}
	)
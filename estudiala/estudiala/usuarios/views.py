from django.shortcuts import render, redirect, render_to_response
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewUserCreationForm, UserInformationForm

def signup(request):
	form = NewUserCreationForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request,'signup.html', {'form' : form})

def signin(request):
	if request.method =='POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			access = authenticate(username=username, password=password)
			if access is not None:
				if access.is_active:
					login(request,access)
					return redirect('information')
				else:
					return redirect('noactive.html')
			else:
				return redirect('nouser.html')
	else:
		form = AuthenticationForm()
	return render(request,'signin.html',{'form':form})

@login_required(login_url='signin')
def information(request):
	form = UserInformationForm(request.POST or None)
	user = request.user

	if form.is_valid():
		form.save(user=request.user)

	return render(request,'info.html', {'form' : form})

@login_required(login_url='signin')
def close(request):
	logout(request)
	return redirect('signin')
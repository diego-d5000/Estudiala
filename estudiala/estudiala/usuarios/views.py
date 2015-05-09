from django.shortcuts import render, redirect
#from django.core.urlresolvers import reverse
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django.views.generic import View
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import NewUserCreationForm, UserInformationForm

def signup(request):
	form = NewUserCreationForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request,'signup.html', {'form' : form})

def information(request):
	form = UserInformationForm(request.POST or None)
	user = request.user

	if form.is_valid():
		form.save(user=request.user)

	return render(request,'info.html', {'form' : form})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#from django.contrib.auth import views as auth_views

#from . import views
# Create your views here.

def login(request):
	return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login.html')
        else:
            #this means the form is not valid
            #so you need to provide the varibles as they were submitted, so the user can change it to proper values
            form = UserCreationForm(request.POST)
    else:
        #this is when the user sends get request 
        form = UserCreationForm()
    return render(request, 'signup_form.html', {'form': form})


    
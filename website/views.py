# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
#from django.contrib.auth import views as auth_views

#from . import views
# Create your views here.

def login(request):
	return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profiles(request):
    return render(request, profiles.html)

# def signup(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             userObj = form.cleaned_data
#             username = userObj['username']
#             #email =  userObj['email']
#             password =  userObj['password']
#             if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
#                 User.objects.create_user(username,password)
#                 user = authenticate(username = username, password = password)
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 raise forms.ValidationError('Looks like a username with that email or password already exists')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'signup_form.html', {'form': form})

def index(request):
    return render(request, 'index.html')

    
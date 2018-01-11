# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.shortcuts import redirect
#from django.contrib.auth import views as auth_views

#from . import views
# Create your views here.

def loginReq(request):
    print('login called')
    if request.method == 'POST':
        print("in login")
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(username,password, 'in login')
            if user is not None:
                print("in login")
                login(request,user)
                return redirect('profiles')
            else:
                return render(request, 'login_form.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'login_form.html', {'form': form})

def profiles(request):
    return render(request, 'profiles.html')

def signupReq(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print('in signup')
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists()):
                User.objects.create_user(username,email = None, password=password)
                user = authenticate(username = username, password = password)
                login(request,user)
                return redirect('profiles')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
                return render(request, 'signup_form.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'signup_form.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def careers(request):
    return render(request, 'careers.html')

    
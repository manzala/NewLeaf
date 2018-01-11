from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserForm(forms.ModelForm):
# 	class Meta:
#    		 model = User
#     	fields = ['first_name', 'last_name', 'email']

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#     	model = User
#     	fields = ('email', 'password')

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')

#     class Meta:
#         model = User
#         fields = ('username', 'password')
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
	)
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )




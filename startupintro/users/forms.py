from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import User
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	


	class Meta:
		model = User
		field = ['username','email','password']

class LoginForm(AuthenticationForm):
	email = forms.EmailField(max_length=225)
	password = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model=User

class RegistrationForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(max_length=225)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserForm
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth import logout


class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.username = 'Bucky'

def login(request):
	# if this is a POST request we need to process the form data
	if user.is_authenticated:
		return redirect('/dashboard')
	else:
		if request.method == 'POST':
		# create a form instance and populate it with data from the request
			form = LoginForm(request.POST)
			#check whether it's valid:
			if form.is_valid():
				email = form.cleaned_data['email']
				password = form.cleaned_data['password']


				return HttpResponseRedirect('/thanks/')

		# if a GET ( or any other method) we'll create a blank form
		return render(request, 'pages/login.html', {})


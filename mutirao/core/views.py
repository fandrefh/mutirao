from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import UserForm, UserProfileForm

# Create your views here.

def home(request):
	return render(request, 'base.html')

def cadastro_usuario(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'foto' in request.FILES:
				profile.foto = request.FILES['foto']

			profile.save()
			return redirect('core:usuariosucesso')
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'core/cadastro_usuario.html',\
		{'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponse("Login feito com sucesso.")
			else:
				return HttpResponse("Sua conta esta desativada.")
		else:
			return HttpResponse("Usuario ou senha invalido.")
	return render(request, 'core/form_login.html')

def sucesso_usuario(request):
	return render(request, 'core/sucesso_usuario.html')
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user', 'data_cadastro')
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, required=True, help_text="Enter your first name")
	last_name = forms.CharField(max_length=20, required=True, help_text="Enter your last name")
	email = forms.EmailField(max_length=100, help_text="Enter your email address")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
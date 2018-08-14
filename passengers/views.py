from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from .models import Passenger
from . forms import SignupForm
from passengers.tokens import account_activation_token

class PassengerList(LoginRequiredMixin, generic.ListView):
	model = Passenger
	template_name = "passengers/passenger_list.html"

	def get_context_data(self, **kwargs):
		context = super(PassengerList, self).get_context_data(**kwargs)
		context['passenger_list_view'] = "True"
		return context


class PassengerDetailView(LoginRequiredMixin, generic.DetailView):
	model = Passenger
	template_name = "passengers/passenger_detail.html"

	def get_context_data(self, **kwargs):
		context = super(PassengerDetailView, self).get_context_data(**kwargs)
		context['passenger_detail_view'] = "True"
		return context


# CRUD
class PassengerCreateView(LoginRequiredMixin, CreateView):
	model = Passenger
	fields = "__all__"


class PassengerUpdateView(LoginRequiredMixin, UpdateView):
	model = Passenger
	fields = "__all__"


class PassengerDeleteView(LoginRequiredMixin, DeleteView):
	model = Passenger
	success_url = reverse_lazy("passenger-list")


def signup_view(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)

			subject = "Activate your Django Flyways account"
			message = render_to_string('account_activation_email.html', {
				"user": user,
				"domain": current_site.domain,
				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
				"token": account_activation_token.make_token(user)
			})

			user.email_user(subject, message)
			return redirect("account_activation_sent")
	else:
		form = SignupForm()
	return render(request, "registration/signup.html", {'form': form})


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
		print(user)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if account_activation_token.check_token(user, token):
		print('CHECKED')
	else:
		print('WRONG VALUE')
		print(token)
		print(user)
		print(uidb64)

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('flights_list')
	else:
		return render(request, 'registration/account_activation_invalid.html')


def account_activation_sent(request):
	return render(request, "registration/account_activation_sent.html")
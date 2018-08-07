from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import Passenger
from . forms import SignupForm

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
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect("flights_list")
	else:
		form = SignupForm()
	return render(request, "registration/signup.html", {'form': form})
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from .models import Passenger

class PassengerList(LoginRequiredMixin, generic.ListView):
	model = Passenger
	template_name = "passengers/passenger_list.html"


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
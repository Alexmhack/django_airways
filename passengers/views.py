from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Passenger

class PassengerList(LoginRequiredMixin, generic.ListView):
	model = Passenger
	template_name = "passengers/passenger_list.html"
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Flight

from datetime import datetime

class HomePageView(generic.ListView):
	model = Flight
	template_name = "flights/home_page.html"

	def get_queryset(self):
		return Flight.objects.filter(status__exact="a").filter(departure__gte=datetime.now())[:5]


class FlightListView(generic.ListView):
	model = Flight
	template_name = "flights/flights_list.html"
	
	def get_queryset(self):
		return Flight.objects.filter(status__exact="a").order_by("-departure")


class FlightDetailView(generic.DetailView):
	model = Flight
	template_name = "flights/flight_detail.html"

	def get_queryset(self):
		return Flight.objects.filter(status__exact="a").filter(departure__gte=datetime.now())


def search_results_view(request):
	query = request.GET['search_query']
	context = {
		"query": query
	}
	return render(request, "flights/search_results.html", context)


def contact_view(request):
	if request.method == "POST":
		try:
			contact_name = request.POST.get("name")
			contact_email = request.POST.get("email")
			context = {
				"contact_name": contact_name,
				"contact_email": contact_email
			}

			return render(request, "flights/contact_form_submit.html", context)
		except Exception as e:
			error = e
			return render(request, "flights/contact_form_submit.html", {'error': error})
	else:
		return render(request, "flights/contact_form.html")


# Flights CRUD
class FlightCreateView(LoginRequiredMixin, CreateView):
	model = Flight
	fields = "__all__"


class FlightUpdateView(LoginRequiredMixin, UpdateView):
	model = Flight
	fields = "__all__"


class FlightDeleteView(LoginRequiredMixin, DeleteView):
	model = Flight
	success_url = reverse_lazy('flights_list')
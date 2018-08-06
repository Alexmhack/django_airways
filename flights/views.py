from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Flight

def home_page(request):
	latest_flights = Flight.objects.filter(status__exact="a")[:6]
	return render(request, "flights/home_page.html", context={'latest_flights': latest_flights})


class FlightListView(generic.ListView):
	model = Flight
	paginate_by = 10

	template_name = "flights/flights_list.html"
	
	def get_queryset(self):
		return Flight.objects.filter(status__exact="a")
		

def flight_detail(request, id):
	flight = Flight.objects.get(pk=id)
	context = {
		'flight': flight
	}

	return render(request, "flights/flight_detail.html", context)


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
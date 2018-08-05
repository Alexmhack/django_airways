from django.shortcuts import render

from .models import Flight

def home_page(request):
	latest_flights = Flight.objects.filter(status__exact="a")[:6]
	return render(request, "flights/home_page.html", context={'latest_flights': latest_flights})


def flights_list(request):
	flights_list = Flight.objects.filter(status__exact="a")
	context = {
		'flights_list': flights_list,
	}
	
	return render(request, 'flights/flights_list.html', context)


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
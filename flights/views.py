from django.shortcuts import render

from .models import Flight

def flights_list(request):
	flights_list = Flight.objects.filter(status__exact="a")
	context = {
		'flights_list': flights_list,
	}
	
	return render(request, 'flights/flights_list.html', context)


def flight_detail(request, pk):
	flight = Flight.objects.get(pk=pk)
	context = {
		'flight': flight
	}

	return render(request, "flights/flight_detail.html", context)
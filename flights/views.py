from django.shortcuts import render

from .models import Flight

def flights_list(request):
	flights_list = Flight.objects.all()
	context = {'flights_list': flights_list}
	return render(request, 'flights/flights_list.html', context)
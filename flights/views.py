from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from .models import Flight
from .forms import ContactForm

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
	contact_form = ContactForm

	if request.method == "POST":
		form = contact_form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			try:
				form_content = request.POST.get('content', '')
			except Exception as e:
				pass

			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content
			}

			content = template.render(context)

			email = EmailMessage(
				"New Contact Form Submission",
				content,
				"Your Django App ",
				["pranavg456@gmail.com"],
				headers={'Reply-To': contact_email}
			)

			notify_template = get_template("contact_soon_template.txt")
			notify_context = {
				"flight_detail": "FLIGHT",
				"content": form_content
			}
			notify_content = notify_template.render(notify_context)

			contact_soon_email = EmailMessage(
				"Django Flyways",
				notify_content,
				"Django Flyways Team",
				[contact_email],
			)

			email.send()
			contact_soon_email.send()
			return render(request, 'contact_confirm.html', context)

	return render(request, 'contact_form.html', {'contact_form': contact_form})


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


# admin accessible views only
class AllFlightView(LoginRequiredMixin, generic.ListView):
	model = Flight
	template_name = "flights/all_flights_list.html"

	def get_context_data(self, **kwargs):
		context = super(AllFlightView, self).get_context_data(**kwargs)
		context['flight_list_view'] = "True"
		return context


class EachFlightDetail(LoginRequiredMixin, generic.DetailView):
	model = Flight
	template_name = "flights/each_flight_detail.html"

	def get_context_data(self, **kwargs):
		context = super(EachFlightDetail, self).get_context_data(**kwargs)
		context['flight_detail_view'] = "True"
		return context
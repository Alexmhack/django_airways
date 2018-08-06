from django.urls import path

from .views import (
	FlightListView,
	flight_detail,
	home_page,
	search_results_view,
	contact_view
)

urlpatterns = [
	path('flights/list/', FlightListView.as_view(), name='flights_list'),
	path("flight/<int:id>/detail/", flight_detail, name="flight_detail"),
	path("", home_page, name="home_page"),
	path("search/results/", search_results_view, name="search_results"),
	path("contact/", contact_view, name="contact_form"),
]
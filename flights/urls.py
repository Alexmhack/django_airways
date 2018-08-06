from django.urls import path

from .views import (
	FlightListView,
	FlightDetailView,
	FlightUpdateView,
	HomePageView,
	search_results_view,
	contact_view,
	FlightCreateView,
	FlightDeleteView,
	AllFlightView,
	EachFlightDetail,
)

urlpatterns = [
	path('flights/list/', FlightListView.as_view(), name='flights_list'),
	path("flight/<int:pk>/detail/", FlightDetailView.as_view(), name="flight_detail"),
	path("", HomePageView.as_view(), name="home_page"),
	path("search/results/", search_results_view, name="search_results"),
	path("contact/", contact_view, name="contact_form"),
]

# Flight CRUD urls
urlpatterns += [
	path('flight/create/', FlightCreateView.as_view(), name="flight-create"),
	path('flight/<int:pk>/update/', FlightUpdateView.as_view(), name="flight-update"),
	path('flight/<int:pk>/delete/', FlightDeleteView.as_view(), name="flight-delete"),
]

urlpatterns += [
	path('flyways/flights/list', AllFlightView.as_view(), name="admin-flights"),
	path("flyways/flights/<int:pk>/detail/", EachFlightDetail.as_view(), name="admin-flight-details"),
]
from django.urls import path

from .views import (
	PassengerList,
	PassengerDetailView,
	PassengerCreateView,
	PassengerDeleteView,
	PassengerUpdateView,
)

urlpatterns = [
	path('list/', PassengerList.as_view(), name="passenger-list"),
	path('<int:pk>/detail/', PassengerDetailView.as_view(), name="passenger-detail"),
	path('create/', PassengerCreateView.as_view(), name="passenger-create"),
	path('delete/', PassengerDeleteView.as_view(), name="passenger-delete"),
	path('update/', PassengerUpdateView.as_view(), name="passenger-update"),
]
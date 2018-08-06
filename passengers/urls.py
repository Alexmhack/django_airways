from django.urls import path

from .views import (
	PassengerList
)

urlpatterns = [
	path('list/', PassengerList.as_view(), name="passenger-list"),
]
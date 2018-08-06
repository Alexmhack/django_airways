from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from flights.models import Flight

class Passenger(models.Model):
	passenger = models.ForeignKey(User, help_text="Passenger for the flight", on_delete=models.SET_NULL, null=True)
	flight = models.ForeignKey(Flight, help_text="Flight for the passenger", on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.passenger} is travelling with {self.flight}"

	def get_absolute_url(self):
		return reverse("passenger-detail", args=[str(self.id)])
from django.db import models

from flights.models import Flight

class Passenger(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField()
	flight = models.ForeignKey(Flight, help_text="Select a flight for the passenger", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.first_name} {self.last_name} is travelling from {self.flight}"
from django.db import models
from datetime import datetime

current_time = datetime.now()

class Flight(models.Model):
	origin = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=10000)
	departure = models.DateTimeField()
	duration = models.DurationField(
		help_text="Duration for flight in hh:mm:ss format"
	)

	FLIGHT_STATUS = (
		('m', 'Maintenance'),
		('d', 'Delay'),
		('a', 'Available'),
		('f', 'Full'),
		('c', 'Cancel'),
	)

	status = models.CharField(max_length=1, choices=FLIGHT_STATUS, default='a', help_text="Flight Availability")

	def __str__(self):
		return f"Flight: {self.origin} to {self.destination}"
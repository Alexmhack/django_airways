from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse

current_time = datetime.now()

class Flight(models.Model):
	origin = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=10000)
	departure = models.DateTimeField(default=current_time + timedelta(hours=2))
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

	@property
	def has_departed(self):
		if self.departure > current_time.now():
			return True
		return False

	def get_absolute_url(self):
		return reverse("flight_detail", args=[str(self.id)])
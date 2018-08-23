from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse
from django.contrib.auth.models import User

current_time = datetime.now()

class FlightModelManager(models.Manager):
	def refresh_departure_time(self, flights=None):
		qs = Flight.objects.filter(id__gte=1)
		if flights is not None and isinstance(flights, int):
			qs = qs.order_by('-id')[:flights]
		new_time = current_time + timedelta(hours=5)
		objects_refreshed = 0
		for q in qs:
			q.departure = new_time
			print(q.id, q.departure)
			q.save()
			objects_refreshed += 1
		return f"New Time: {new_time} For: {objects_refreshed} flights"


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

	objects = FlightModelManager()

	def __str__(self):
		return f"Flight: {self.origin} to {self.destination}"

	@property
	def has_departed(self):
		if self.departure < current_time.now():
			return True
		return False

	def get_absolute_url(self):
		return reverse("flight_detail", args=[str(self.id)])

	@property
	def departure_format(self):
		return self.departure.strftime("On %A %d %B, %y at %H:%M")

	@property
	def get_departure_time(self):
		departure_in = self.departure - current_time
		return self.departure.time().strftime("%H:%M %p")

	@property
	def get_arrival_time(self):
		arrival_in = self.departure + self.duration
		return arrival_in.strftime("On %A %d %B, %y at %H:%M %p")

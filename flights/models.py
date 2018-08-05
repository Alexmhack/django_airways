from django.db import models

class Flight(models.Model):
	origin = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	duration = models.DurationField(
		help_text="Duration for flight in minutes"
	)

	FLIGHT_STATUS = (
		('m', 'Maintenance'),
		('d', 'Delay'),
		('a', 'Available'),
		('f', 'Full'),
		('c', 'Cancel'),
	)

	status = models.CharField(max_length=1, choices=FLIGHT_STATUS, default='a', help_text="Flight Availability")

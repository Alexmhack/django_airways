from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from flights.models import Flight

class Passenger(models.Model):
	passenger = models.ForeignKey(User, help_text="Passenger for the flight", on_delete=models.SET_NULL, null=True)
	flight = models.ForeignKey(Flight, help_text="Flight for the passenger", on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.passenger} is travelling with {self.flight}"

	def get_absolute_url(self):
		return reverse("passenger-detail", args=[str(self.id)])


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=100, blank=True)
	location = models.CharField(max_length=15, blank=True)
	email_confirm = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
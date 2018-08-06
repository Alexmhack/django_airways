from django.contrib import admin

from .models import Passenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
	list_display = ('passenger', 'flight')
	search_fields = ('passenger', 'flight')
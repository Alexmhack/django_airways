from django.contrib import admin

from .models import Flight

class FlightAdmin(admin.ModelAdmin):
	list_display = ('origin', 'destination', 'duration', 'status')
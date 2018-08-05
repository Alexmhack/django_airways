from django.contrib import admin

from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
	list_display = ('origin', 'destination', 'duration', 'status')
	search_fields = ('origin', 'destination', 'duration', 'status')
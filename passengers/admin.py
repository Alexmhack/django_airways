from django.contrib import admin

from .models import Passenger

@admin.register(Passenger)
class Passenger(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'flight')
	search_fields = ("first_name", "last_name", "flight")
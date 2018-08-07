from django.contrib import admin

from .models import Passenger, Profile

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
	list_display = ('passenger', 'flight')
	search_fields = ('passenger', 'flight')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'bio', 'email_confirm')
	search_fields = ('user',)
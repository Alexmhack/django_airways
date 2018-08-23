from django.core.management.base import BaseCommand, CommandError

from flights.models import Flight

class Command(BaseCommand):
    help = 'Resfreshes all Flights departure time'

    def add_arguments(self, parser):
        parser.add_argument('flights', type=int)

    def handle(self, *args, **options):
        print(options)
        return Flight.objects.refresh_departure_time(flights=options['flights'])

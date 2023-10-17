from django.contrib.admin import *

from apps.flight.models import Flight
from apps.plane.models import Plane
from apps.airlane.models import Airline

@register(Flight)
class FlightAdmin(ModelAdmin):

    list_display = ('id', 'fro', 'to', 'price')
    list_display_links = ('id', 'fro', 'to', 'price')

@register(Plane)
class PlaneAdmin(ModelAdmin):

    list_display = ('id', 'name', 'capacity')
    list_display_links = ('id', 'name', 'capacity')

@register(Airline)
class AirlineAdmin(ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
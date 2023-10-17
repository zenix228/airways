from django.db.models import *
from apps.plane.models import Plane
from apps.airlane.models import Airline

class Flight(Model):
    fro = CharField(max_length=260)
    to = CharField(max_length=500)
    plane = ForeignKey(Plane, on_delete=CASCADE)
    airline = ForeignKey(Airline, on_delete=CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2)

    
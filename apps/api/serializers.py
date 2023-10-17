from rest_framework.serializers import *
from apps.plane.models import Plane
from apps.airlane.models import Airline
from apps.flight.models import Flight

class PlaneSerializer(ModelSerializer):
    class Meta:

        model = Plane
        fields = '__all__'

class AirlineSerializer(ModelSerializer):
    class Meta:

        model = Airline
        fields = '__all__'

class FlightSerializer(ModelSerializer):
    class Meta:

        model = Flight
        fields = '__all__'
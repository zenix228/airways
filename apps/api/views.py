from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import FlightSerializer, PlaneSerializer, AirlineSerializer

from apps.airlane.models import Airline
from apps.plane.models import Plane
from apps.flight.models import Flight

class FlightAPIView(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = FlightSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class FlightDetailAPIView(APIView):

    def get(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializers = FlightSerializer(flight)
        return Response(
            serializers.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializers = FlightSerializer(flight, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializers.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        Flight.delete()
        return Response('Deleted', status=HTTP_204_NO_CONTENT)
    
class AirlineAPIView(APIView):

    def get(self, request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class AirlineDetailAPIView(APIView):

    def get(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializers = AirlineSerializer(airline)
        return Response(
            serializers.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializers = AirlineSerializer(airline, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializers.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        airline.delete()
        return Response('Deleted', status=HTTP_204_NO_CONTENT)
    
class PlaneAPIView(APIView):

    def get(self, request):
        planes = Plane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = PlaneSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class PlaneDetailAPIView(APIView):

    def get(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializers = PlaneSerializer(plane)
        return Response(
            serializers.data,
            status=HTTP_200_OK
        )
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializers = PlaneSerializer(plane, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data,
                status=HTTP_202_ACCEPTED
            )
        return Response(
            serializers.errors,
            status=HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        plane.delete()
        return Response('Deleted', status=HTTP_204_NO_CONTENT)
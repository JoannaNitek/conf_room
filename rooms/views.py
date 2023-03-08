from django.shortcuts import render
from rest_framework import viewsets
from .models import Room, Reservation
from .serializers import ReservationSerializer, RoomSerializer
# Create your views here.

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # lookup_field = 'room'

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

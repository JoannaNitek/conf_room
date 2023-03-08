from rest_framework import status
from rest_framework.test import APITestCase

from .models import Room
from .serializers import RoomSerializer

# Rooms - lista, szczegóły, modyfikacja, usuwanie

# Reservation - rezerwacja danej sali na ten sam dzień, usunięcie rezerwacji, dodanie rezerwacji
# Wyszukiwanie sali
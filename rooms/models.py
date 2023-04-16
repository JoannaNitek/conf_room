from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    has_projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    person = models.CharField(max_length=30)
    date = models.DateField(blank=False, null=False)
    comment = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, related_name='reservation', on_delete=models.CASCADE)

# możliwość tylko jednej rezerwacji danej sali na dany dzień

    class  Meta:
        unique_together=('room', 'date')
        
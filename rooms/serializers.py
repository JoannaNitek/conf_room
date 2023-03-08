from rest_framework import serializers
from .models import Reservation, Room


#serializacja - proces zamaiany obiektu (modelu django) na JSONa
# HyperlinkedModelSerializer używa hiperłączy zamiast kluczy głównych do reprezentowania relacji

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['id', 'person', 'date', 'comment', 'room']
 

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    reservation = serializers.SlugRelatedField(
        many=True,
        slug_field='date',
        allow_null=True,
        read_only=True
        # queryset=Reservation.objects.all()
    )
    # reservation = serializers.HyperlinkedIdentityField(view_name='api:reservations-list', lookup_field='room')

    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'has_projector', 'reservation']

    # def create(self, validated_data):
    #     return Room(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.capacity = validated_data.get('capacity', instance.capacity)
    #     instance.has_projector = validated_data.get('has_projector', instance.has_projector)
    #     instance.save()
    #     return instance

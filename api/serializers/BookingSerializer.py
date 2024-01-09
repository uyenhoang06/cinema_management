from rest_framework import serializers

from cinemaa.models import ShowTime
from rest_framework.relations import StringRelatedField

from booking.models import Booking


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = ['customer', ]





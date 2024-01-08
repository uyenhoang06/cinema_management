
from rest_framework import serializers

from cinemaa.models import ShowTime


class ShowtimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTime
        fields = ['movie', 'hall', 'date', 'start_time', 'end_time', 'slot_status', 'subtitle']



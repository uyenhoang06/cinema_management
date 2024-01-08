from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cinemaa.models import ShowTime
from ..serializers.ShowtimeSerializer import ShowtimeSerializer


class ShowtimeView(APIView):

    def get(self, request):
        showtime = ShowTime.objects.all()
        serializer = ShowtimeSerializer(showtime, many=True)
        return Response(serializer.data)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.RegisterSerializer import RegisterSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create()
            return Response({'Register successfully': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
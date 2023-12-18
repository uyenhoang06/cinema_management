from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from .serializer import UserRegisterSerializer
from rest_framework.response import Response
from .email import sendOTP
from .models import OneTimePassword


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            sendOTP(user['email'])
            return Response({
                'data' : user,
                'message' : f'A passcode has been sent to your email'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(APIView):
    def post(self, request):
        try:
            passcode = request.data.get('otp')
            user_pass_obj=OneTimePassword.objects.get(otp=passcode)
            user=user_pass_obj.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({
                    'message':'account email verified successfully'
                }, status=status.HTTP_200_OK)
            return Response({'message':'passcode is invalid user is already verified'}, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist as identifier:
            return Response({'message':'passcode not provided'}, status=status.HTTP_400_BAD_REQUEST)

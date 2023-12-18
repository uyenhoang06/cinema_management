
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView, VerifyUserEmail


urlpatterns = [
    path('api/register', RegisterUserView.as_view(), name = 'register'),
    path('api/verify', VerifyUserEmail.as_view(), name='verify')
]
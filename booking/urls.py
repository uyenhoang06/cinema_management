
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('book_showtime/<int:id>', BookingView.as_view(), name='booking'),
    path('payment/<int:id>', PaymentView.as_view(), name='payment'),
    path('list_booking', ListBooking.as_view(), name='list_booking'),

    path('search_result/', ListBooking.as_view(), name='search_result'),

    # path('search_result/ticket/payment_detail/<int:id>', ListBooking.as_view())

]



from django.contrib import admin
from django.urls import path, include

from api.views.MovieView import MovieView
from api.views.RegisterView import RegisterView
from api.views.ShowtimeView import ShowtimeView
# from api.views.BookingView import BookingView

urlpatterns = [
    path('api/film/', MovieView.as_view()),
    path('api/film/<int:id>', MovieView.as_view()),

    path('api/register/', RegisterView.as_view()),

    path('api/showtime/', ShowtimeView.as_view()),
    path('api/showtime/<int:id>', ShowtimeView.as_view()),

    # path('api/booking/', BookingView.as_view()),

]

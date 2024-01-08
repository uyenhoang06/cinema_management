from collections import defaultdict

from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta, date

from .forms import *
from booking.models import *


from .serializer import MovieSerializer
#
from movie.models import *

# Create your views here.


class HomeView(View):
    template_name = "home.html"
    Model = Movie

    def list_movie(self):
        items = []
        for i, movie in enumerate(Movie.objects.all()):
            item = {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'trailer': movie.trailer,
                'poster': movie.poster,
                'banner': movie.banner,
                'age': movie.age,
                'rating': movie.rating,
                'status': movie.status,
                'released_date': movie.released_date,
                'director': movie.director,
                'actor': movie.actor,
                'language': movie.language,
                'country': movie.country,
                'duration': movie.duration,
                'genre': movie.genre
            }
            # print(item)
            items.append(item)
        return items

    def get(self, request):

        context = {
            'movies' : self.list_movie(),
            'current_tab' : 'home'
        }

        return TemplateResponse(request, self.template_name, context)


class ShowtimeView(View):
    template = 'schedule.html'

    def get_showtime(self, date):
        # print(today)
        showtimes = []
        # for i, showtime in enumerate(ShowTime.objects.filter(date__gte=today, date__lte=today+timedelta(days=7))):
        for i, showtime in enumerate(ShowTime.objects.filter(date=date, date__lte=date+timedelta(days=5))):
            item = {
                'id' : showtime.id,
                'movie': showtime.movie,
                'hall': showtime.hall,
                'date': showtime.date,
                'start_time': showtime.start_time,
                'end_time': showtime.end_time,
                'slot_status': showtime.slot_status,
                'subtitle': showtime.subtitle
            }
            # print(item)
            showtimes.append(item)
        return showtimes

    def get(self, request):
        today = datetime.date.today()
        today_date = date.today()

        showtime_today = self.get_showtime(today)
        movies_today = set([showtime['movie'] for showtime in showtime_today])
        list_showtime_today = []
        for movie in movies_today:
            dict = defaultdict(list)
            for showtime in showtime_today:
                if showtime['movie'] == movie:
                    for key, value in showtime.items():
                        dict[key].append(value)
                    list_showtime_today.append(dict)

        context = {
            'today' : today_date,
            'showtime_today' : showtime_today,

            'next1' : today_date+timedelta(days=1),
            'showtime_next1': self.get_showtime(today + timedelta(days=1)),

            'next2': today_date + timedelta(days=2),
            'showtime_next2': self.get_showtime(today + timedelta(days=2)),

            'next3': today_date + timedelta(days=3),
            'showtime_next3': self.get_showtime(today + timedelta(days=3)),

            'next4': today_date + timedelta(days=4),
            'showtime_next4': self.get_showtime(today + timedelta(days=4)),

            'next5': today_date + timedelta(days=5),
            'showtime_next5': self.get_showtime(today + timedelta(days=5)),
            'current_tab' : 'schedule'
        }

        return TemplateResponse(request, self.template, context)


@method_decorator([
    login_required(login_url='/login'),
    permission_required('cinemaa.add_showtime', raise_exception=True),
], name='dispatch')
class AddShowtimeView(View):
    template = 'add_schedule.html'

    def get(self, request):
        context = {
            'form': ShowTimeForm(),
        }
        return TemplateResponse(request, self.template, context)

    def post(self, request):
        form = ShowTimeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect("/schedule")


@login_required(login_url='/login')
@permission_required('cinemaa.change_showtime', raise_exception=True)
def update_showtime(request, id):
    showtime = ShowTime.objects.get(id=id)
    form = ShowTimeForm(instance=showtime)

    if request.method == "POST":
        form = ShowTimeForm(request.POST, request.FILES, instance=showtime)
        if form.is_valid():
            showtime.movie = form.cleaned_data['movie']
            showtime.hall = form.cleaned_data['hall']
            showtime.date = form.cleaned_data['date']
            showtime.start_time = form.cleaned_data['start_time']
            showtime.end_time = form.cleaned_data['end_time']
            showtime.slot_status = form.cleaned_data['slot_status']
            showtime.subtitle = form.cleaned_data['subtitle']
            showtime.save()
            # form.save()
            return HttpResponseRedirect('/schedule')

    return render(request, "update_schedule.html", {"form": form})


@login_required(login_url='/login')
@permission_required('cinemaa.delete_showtime', raise_exception=True)
def delete_showtime(request, id):
    show = ShowTime.objects.get(id=id)
    show.delete()
    request.session['delete_showtime'] = 'Delete showtime successfully'
    return HttpResponseRedirect('/schedule')



from booking.models import *
from account.models import *
@method_decorator([
    login_required(login_url='/login'),
], name='dispatch')
class TicketView(View):
    template_name = "ticket.html"

    def list_booking(self, user):
        list_booking = []
        # for i, showtime in enumerate(ShowTime.objects.filter(date__gte=today, date__lte=today+timedelta(days=7))):
        for i, booking in enumerate(Booking.objects.filter(customer=user)):
                item = {
                    "id" : booking.id,
                    "created_at" : booking.created_at,
                    "score" : booking.score,
                    'status' : booking.booking_status
                    # "price" : ticket.ticket_price,
                    # "showtime" : ticket.showtime,
                    # "seat" : ticket.seat,
                }
                list_booking.append(item)
        return list_booking

    def get(self, request):
        today = datetime.date.today()

        user = User.objects.get(username=request.user)
        list_booking = self.list_booking(user)
        ongoing_booking = []
        success_booking = []
        for booking in list_booking:
            if booking['status'] == 'on-going':
                ongoing_booking.append(booking)
            elif booking['status'] == 'successful':
                success_booking.append(booking)

        success_booking = sorted(success_booking, key= lambda x: x['created_at'], reverse=True)

        context = {
            'current_tab': 'ticket',
            'booking' : list_booking,
            'ongoing_booking' : ongoing_booking,
            'success_booking' : success_booking,
            'user' : user,
        }
        return TemplateResponse(request, self.template_name, context)


@login_required(login_url='/login')
def delete_ticket(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect('/ticket')

@login_required(login_url='/login')
def payment_detail(request, id):
    booking = Booking.objects.get(id=id)
    ticket = Ticket.objects.filter(booking=booking)
    return render(request, 'payment_detail.html', {
        'booking' : booking,
        'ticket' : ticket
    })


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {
        'ticket' : ticket,
    })


@api_view(['GET'])
def api_get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_post_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Create movie successfully' : serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_movie(request, id):
    movie = Movie.objects.get(id = id)
    serializer = MovieSerializer(instance=movie, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'update movie' : serializer.data})
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_movie(request, id):
    movie = Movie.objects.get(id = id)
    movie.delete()

    return Response(f"Successful delete movie")


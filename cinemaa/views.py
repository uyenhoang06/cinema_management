from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer

from .form.movieForm import MovieForm
from .models import Movie

# Create your views here.
def get_items(self):
    items = []
    for i, movie in enumerate(Movie.objects.all()):
        item = {
            'movie_id': movie.movie_id,
            'title': movie.title,
            'description': movie.description,
            'trailer': movie.trailer,
            'poster': movie.poster,
            'age': movie.age,
            'rating': movie.rating,
            'cost': movie.cost,
            'status': movie.status,
            'released_year': movie.released_year,
            'director': movie.director,
            'producer': movie.producer,
            'language': movie.language,
            'genre': movie.genre
        }

        items.append(item)
    return items

class HomeView(View):
    template_name = "home.html"
    Model = Movie

    def get(self, request):
        context = {
            'items' : get_items(request),
            'current_tab' : 'home'
        }

        return TemplateResponse(request, self.template_name, context)


def schedule(request):
    return render(request, "schedule.html", context={"current_tab": "schedule"})

def ticket(request):
    return render(request, "ticket.html", context={"current_tab": "ticket"})


def add_film(request):
    submitted = False
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return HttpResponseRedirect("/film?submitted=True")
    else:
        form = MovieForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_film.html", {"form" : form, "submitted":submitted})

def update_film(request, id):
    movie = Movie.objects.get(movie_id=id)
    form = MovieForm(instance=movie)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/film')

    return render(request, "update_film.html", {"form" : form})

def delete_film(request, id):
    movie = Movie.objects.get(movie_id = id)
    movie.delete()
    return HttpResponseRedirect('/film')




class MovieView(View):
    template_name = "film.html"
    Model = Movie

    def get(self, request):
        context = {
            'items' : get_items(request),
            'current_tab' : 'film'
        }

        return TemplateResponse(request, self.template_name, context)



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
        return Response({'create movie' : serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def api_update_movie(request, id):
    movie = Movie.objects.get(movie_id = id)
    serializer = MovieSerializer(instance=movie, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'update movie' : serializer.data})
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_movie(request, id):
    movie = Movie.objects.get(movie_id = id)
    movie.delete()

    return Response("Successful delete")


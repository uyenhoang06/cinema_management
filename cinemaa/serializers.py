from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title', 'description', 'trailer', 'poster', 'age', 'rating', 'cost', 'status', 'released_year', 'director', 'producer', 'language', 'genre']


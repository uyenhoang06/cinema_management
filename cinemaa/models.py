from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    # trailer = models.CharField(max_length=100, blank=True)
    trailer = models.FileField(upload_to='video/', blank=True)
    poster = models.ImageField(blank=True, upload_to="images/")
    age = models.IntegerField(blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    cost = models.IntegerField(blank=True)
    status = models.BooleanField(blank=True)
    released_year = models.IntegerField(blank=True)
    director = models.CharField(max_length=100, blank=True)
    producer = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

from django import forms
from django.forms import ModelForm
from ..models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'description', 'trailer', 'poster', 'age', 'rating', 'cost', 'status',
                  'released_year', 'director', 'producer', 'language', 'genre')
        widgets = {
            "movie_id": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "description": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "trailer": forms.FileInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "poster": forms.FileInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "rating": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "cost": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "status": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "released_year": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "director": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "producer": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "language": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),
            "genre": forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""}),

        }

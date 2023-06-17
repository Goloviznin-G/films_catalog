from django import forms
from django.forms import ModelForm

from data_films.Models.Films.films import Films


class Create_new_genre(forms.Form):
    genre = forms.CharField(label="Введите новый жанр", max_length=255)

class Create_new_director(forms.Form):
    name = forms.CharField(label="Введите имя нового режиссера", max_length=255)
    last_name = forms.CharField(label="Введите фамилию нового режиссера", max_length=255)

class Create_new_film(ModelForm):

    class Meta:
        model = Films
        fields = ['name', 'year', 'genres', 'directors']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'genres' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'directors' : forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Название фильма',
            'year': 'Год выхода',
            'genres': 'Жанры фильма',
            'directors': 'Режиссер'
        }

class Edit_film(ModelForm):

    class Meta:
        model = Films
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'directors': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Название фильма',
            'year': 'Год выхода',
            'genres': 'Жанры фильма',
            'directors': 'Режиссер'
        }


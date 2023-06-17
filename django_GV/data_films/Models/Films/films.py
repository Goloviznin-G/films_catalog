from django.db import models

from .validators import validate_date, validate_name
from ..Directors.directors import Directors
from ..Genres.genres import Genres
# from ..Films_Genres.films_genres import Films_Genres
# from ..Films_Directors.films_directors import Films_Directors


class Films(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=255, validators=[validate_name]) # blank=True
    year = models.CharField(max_length=4, validators=[validate_date])
    genres = models.ManyToManyField(Genres, through='Films_Genres')
    directors = models.ManyToManyField(Directors, through='Films_Directors')

    class Meta:
        managed = False
        db_table = 'films'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.year}; '



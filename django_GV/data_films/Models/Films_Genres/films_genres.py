from django.db import models
from ..Films.films import Films
from ..Genres.genres import Genres

class Films_Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    film_id = models.ForeignKey(Films, on_delete=models.CASCADE, db_column='film_id')
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE, db_column='genre_id')

    class Meta:
        managed = False
        db_table = 'films_genres'

from django.db import models
from ..Directors.directors import Directors
from ..Films.films import Films

class Films_Directors(models.Model):
    id = models.BigAutoField(primary_key=True)
    film_id = models.ForeignKey(Films, on_delete=models.CASCADE, db_column='film_id')
    director_id = models.ForeignKey(Directors, on_delete=models.CASCADE, db_column='director_id')

    class Meta:
        managed = False
        db_table = 'films_directors'

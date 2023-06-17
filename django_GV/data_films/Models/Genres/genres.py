from django.db import models


class Genres(models.Model):
    id = models.BigAutoField(primary_key = True)
    genre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'genres'

    def __str__(self):
        return f'{self.id}. {self.genre}'
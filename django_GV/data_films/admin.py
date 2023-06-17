from django.contrib import admin

from .Models.Directors.directors import Directors
from .Models.Films.films import Films
from .Models.Films_Directors.films_directors import Films_Directors
from .Models.Films_Genres.films_genres import Films_Genres
from .Models.Genres.genres import Genres


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year']
    list_filter = ['year']

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['id', 'genre']

@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name']

@admin.register(Films_Directors)
class Films_DirectorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'film_id', 'director_id']

@admin.register(Films_Genres)
class Films_GenresAdmin(admin.ModelAdmin):
    list_display = ['id', 'film_id', 'genre_id']

# admin.site.register(Films_Directors)
# admin.site.register(Films_Genres)
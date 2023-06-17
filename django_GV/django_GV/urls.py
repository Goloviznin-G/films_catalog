"""django_GV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from data_films.views import index, film, catalog, create_new_genre, create_new_film, edit_film, del_film, del_genre, del_dir, create_new_dir
from register.views import register, log_in

urlpatterns = [
    #основное
    path('', index),
    path('film/', catalog, name='catalog'),
    path('film/<int:film_id>', film),

    #фильмы
    path('film/edit/<int:film_id>', edit_film),
    path('film/del_film/<int:film_id>', del_film),
    path('film/create/', create_new_film),

    #жанры
    path('del_genre/<int:genre_id>', del_genre),
    path('genre/create/', create_new_genre),

    #режиссеры
    path('del_dir/<int:dir_id>', del_dir),
    path('director/create/', create_new_dir),

    #админка
    path('admin/', admin.site.urls), #admin, admin
    path('register/', register),
    path('login/', log_in),
]

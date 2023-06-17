from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from .Models.Directors.directors import Directors
from .Models.Films.films import Films
from .Models.Genres.genres import Genres
from .forms import Create_new_genre, Create_new_film, Create_new_director, Edit_film
from .lib.pagi import calc_pagi, calc_sort, get_url


def index(request):
    return redirect('catalog')


def catalog(request):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    sorting = calc_sort(request)
    order_ = '-' if sorting.get('desc') == 1 else ''
    if search is not None:
        all_obj = Films.objects.filter(name__icontains=search)
    else:
        all_obj = Films.objects.all()
    if sort is not None:
        all_obj = all_obj.order_by(f'{order_}{sort}')
    cur_page = get_url(request)
    # genres = film.genres.all()
    # directors = film.directors.all()
        #all - все, filter - фильтр, __contains - модификатор присутвия значения,
        # __startwith - модификатор "начинается"
        #all = [f'{c.id}: {c.name}, {c.year}' for c in all_obj]

    context = {
        'data': Paginator(all_obj, 7).page(cur_page),
        'search': search,
        'sorting': sorting,
        'pagination': calc_pagi(all_obj, 7, cur_page)
        # 'genres': ', '.join([genre.genre for genre in genres]),
        # 'director_ln': ', '.join([director.last_name for director in directors]),
        # 'director_n': ', '.join([director.name for director in directors]),
    }
    return render(request, 'list_of_films.html', context)


def film(request, film_id):
    film = Films.objects.get(id = film_id)
    genres = film.genres.all()
    directors = film.directors.all()
    data = {
        'film': film,
        'genres': ', '.join([genre.genre for genre in genres]),
        'director_ln': ', '.join([director.last_name for director in directors]),
        'director_n': ', '.join([director.name for director in directors]),
    }
    context = {
        'data': data,
    }
    return render(request, 'film.html', context)


def create_new_genre(request):
    if request.method == 'POST':
        genre = Create_new_genre(request.POST)
        if genre.is_valid():
            genre_name = genre.cleaned_data['genre']
            new_genre = Genres(genre=genre_name)
            new_genre.save()
            return HttpResponse(f'{new_genre.id}')
    else:
        genre = Create_new_genre()
        return render(request, 'create_new_genre.html', {'genre': genre})



def create_new_dir(request):
    if request.method == 'POST':
        director = Create_new_director(request.POST)
        if director.is_valid():
            name = director.cleaned_data['name']
            last_name = director.cleaned_data['last_name']
            new_director = Directors(name=name, last_name=last_name)
            new_director.save()
            return HttpResponse(f'{new_director.id}')
    else:
        director = Create_new_director()
        return render(request, 'create_new_dir.html', {'director': director})



def create_new_film(request):
    if request.method == 'POST':
        form = Create_new_film(request.POST)

        if form.is_valid():
            new_film = Films(
                name=form.cleaned_data['name'],
                year=form.cleaned_data['year'],
            )
            new_film.save()
            new_film.genres.set(form.cleaned_data['genres'])
            new_film.directors.set(form.cleaned_data['directors'])

            return redirect('/film')
        else:
            return render(request, 'create_new_film.html', {'form': form})
    else:
        form = Create_new_film()
        return render(request, 'create_new_film.html', {'form': form})

# def create_new_film(request):
#     if request.method == 'POST':
#         film = Films(
#             name = request.POST.get('name'),
#             year = request.POST.get('year'), # добавить жанры и директора
#             # genre=Genres.objects.get(id=request.POST.get("genre")),
#             # director = Directors.objects.get(id=request.POST.get("director"))
#         )
#         film.save()
#         # film.genres.set(request.POST.get('genres'))
#         # film.directors.set(request.POST.get('directors'))
#         return HttpResponse(f'Удалось добавить новый фильм {film.name}')
#     else:
#
#         genres = Genres.objects.all()
#         directors = Directors.objects.all()
#
#         return render(request, 'create_new_film.html', { 'genres': genres, 'directors' : directors  })


def edit_film(request, film_id):
    film = Films.objects.get(id = film_id)
    form = Edit_film(instance = film)
    if request.method == 'POST':
        form = Edit_film(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('/film')
    else:
        return render(request, 'edit_film.html', {'form': form})

def del_film(request, film_id):
    film = Films.objects.get(id = film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('/film')
    else:
        return render(request, 'del_film.html', {'data' : film})

def del_genre(request, genre_id):
    genre = Genres.objects.get(id = genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('/film')
    else:
        return render(request, 'del_genre.html', {'genre' : genre})

def del_dir(request, dir_id):
    director = Directors.objects.get(id = dir_id)
    if request.method == 'POST':
        director.delete()
        return redirect('/film')
    else:
        return render(request, 'del_dir.html', {'director' : director})

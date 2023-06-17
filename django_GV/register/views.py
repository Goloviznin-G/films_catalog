from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):

  if request.method == "POST":

    user = User.objects.create_user(
      request.POST.get("name"),
      request.POST.get("email"),
      request.POST.get("password")
    )

    user.save()

  return render(request, "register.html")


def log_in(request):

  if request.method == "POST":

    username = request.POST['name']
    password = request.POST['password']
    u = authenticate(request, username=username, password=password)

    if u is not None:
      login(request, u)
      return redirect("/film")
    else:
      return render(request, "login.html")
  else:
    return render(request, "login.html")



from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .decorators import allowed_users, unauthenticated_user


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Main')
        else:
            messages.error(request, 'Username or password incorrect!')
            return redirect('Login')

    context = {}
    return render(request, 'app_forgotten_pw/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def MainView(request):

    context = {}
    return render(request, 'app_forgotten_pw/main.html', context)

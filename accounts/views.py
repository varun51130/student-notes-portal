from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    return redirect('home')


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'register.html',
                {
                    'error': 'Username already exists'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('home')

    return render(
        request,
        'register.html'
    )
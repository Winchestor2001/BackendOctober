from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


def home_page(request):
    info = SiteInfo.objects.first()
    context = {
        'info': info
    }
    return render(request, 'home.html', context)


def register_page(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context['message'] = 'Bunday Email mavjud'
            return render(request, 'register.html', context) 
        
        user = User.objects.create(
            username=email,
            email=email, first_name=first_name, 
            last_name=last_name)
        user.set_password(password)
        user.save()
        return redirect('home')

    return render(request, 'register.html')


def login_page(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            context['message'] = 'Email yoki Parol xato!!!'

    return render(request, 'login.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home_page(request):
    return render(request, 'home.html')


def register_page(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            context['error'] = 'Bunday username mavjud'
            return render(request, 'register.html', context)

        if password == password2:
            user = User.objects.create(username=username, password=password)
            user.first_name = name
            user.set_password(password)
            user.save()
            return redirect('home')
        else:
            context['error'] = 'Parol bir xil emas'

    return render(request, 'register.html', context)









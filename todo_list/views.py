from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo


def register_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            context['error'] = 'Bunday username mavjud'
            return render(request, 'register.html', context)

        if password == password2:
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()
            return redirect('task_list')
        else:
            context['error'] = 'Parol bir xil emas'
    return render(request, 'register.html')


def login_page(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            context['error'] = 'Bunday foydalanuvchi mavjud emas!'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


@login_required(login_url='login')
def task_list(request):
    user_tasks_count = Todo.objects.filter(user=request.user).count()
    context = {
        'user_tasks_count': user_tasks_count,
    }
    return render(request, 'task_list.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')




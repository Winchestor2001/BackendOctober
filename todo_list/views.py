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
    tasks = Todo.objects.filter(user=request.user)
    context = {
        'user_tasks_count': tasks.count(),
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        complated = request.POST.get('complated')
        task = Todo.objects.create(
            user=request.user,
            title=title,
            description=description
        )
        if complated == 'on':
            task.complated = True
        else:
            task.complated = False
        task.save()

        return redirect('task_list')

    return render(request, 'create_task.html')


@login_required(login_url='login')
def delete_task(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect('task_list')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from django.db.models import Q


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


@login_required
def task_list(request):
    q = request.GET.get('q')
    tasks = Todo.objects.filter(user=request.user)

    if q is not None:
        tasks = tasks.filter(Q(title__icontains=q) | Q(description__icontains=q))

    context = {
        'user_tasks_count': tasks.count(),
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')



@login_required
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


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.delete()
    return redirect('task_list')


@login_required
def update_task(request, pk):

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        complated = request.POST.get('complated')
        task = Todo.objects.get(pk=pk)
        task.title = title
        task.description = description
        if complated == 'on':
            task.complated = True
        else:
            task.complated = False
        task.save()
        return redirect('task_list')


    task = get_object_or_404(Todo, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'update_task.html', context)

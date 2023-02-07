from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    ismlar=['Isroil','Boburmirzo','Jahongir','Madina','Gulshoda']
    mevalar=['Olma','Anor','Behi','gilos']
    context={
        'ismlar':ismlar,
        'fruits':mevalar
    }
    return render(request,'home.html',context)
    
import requests
def about(request):
    data=requests.get('https://restcountries.com/v2/all').json()
    context={
        'countries':data
    }
    return render(request,'about.html',context)

@login_required(login_url='login')
def contact(request):
    dataAll=ContactUs.objects.all().order_by('id')
    context={
        'dataAll':dataAll
    }
    if request.method=='POST':
        name=request.POST['fullname']
        contact_number=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['text']
        data=ContactUs(
            fullname=name,phone=contact_number,email=email,
            subject=subject,text=message
        )
        data.save()
        msg=f'Xurmatli {name},Sizning taklif/shikoyatingiz qabul qilindi.'
        context['message']=msg
    return render(request,'contact.html',context)


@login_required(login_url='login')
def category_page(request):
    catgories = Category.objects.all()
    context = {'catgories': catgories}
    return render(request, 'category.html', context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        choose = request.POST['choose']

        user = User.objects.create(
            username=username, email=email
        )
        if choose == 'admin':
            user.is_staff = True
            user.is_superuser = True
        user.set_password(password)
        user.save()
        UserProfile.objects.create(
            user=user,
            phone_number=phone_number
        ).save()
        return redirect('login')
        

    return render(request, 'register.html')


def check_username(request):
    username = request.GET['user']
    user = User.objects.filter(username=username)
    if user.exists():
        text = 'Bor'
    else:
        text = 'Yoq'

    return HttpResponse(text)


def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            context['error'] = 'Bunday foydalanuvchi yoq'
    return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('home-page')


def category_detail(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.views += 1
    category.save()
    context = {'category': category}
    return render(request, 'category_detail.html', context)


# def counter(re)

from django.db import models
import datetime
from django.contrib.auth.models import User

class Student(models.Model):
    gender_type=(
        ('M','Erkak'),('F','Ayol')
    )
    fullname=models.CharField(max_length=100,verbose_name='F.I.O')
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=13,unique=True,verbose_name='Telefon raqam')
    fee=models.FloatField(default=0)
    roll_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=50,choices=gender_type)
    address=models.TextField(blank=True)
    is_registered=models.BooleanField(default=False)
    birthDay=models.DateField(null=True,
    default=datetime.datetime.now())
    # python manage.py makemigrations
    # python manage.py migrate

    class Meta:
        verbose_name_plural='Talabalar'

    def __str__(self):
        return f'{self.fullname} | {self.roll_no}'




class ContactUs(models.Model):
    fullname=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # python manage.py makemigrations
    # python manage.py migrate
    class Meta:
        verbose_name_plural='Takliflar'

    def __str__(self):
        return f'{self.fullname} {self.phone}'

class Category(models.Model):
    cat_name=models.CharField(max_length=50)
    cover_img=models.ImageField(upload_to='category', blank=True, null=True)
    description=models.TextField()
    views = models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # pip install Pillow
    class Meta:
        verbose_name_plural='Kategoriya'
    def __str__(self):
        return self.cat_name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.user)

















class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    author=models.CharField(max_length=100)
    post_view=models.IntegerField()
    created_add=models.DateTimeField(auto_now_add=True)
    updated_add=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Yangiliklar'

    def __str__(self):
        return self.title


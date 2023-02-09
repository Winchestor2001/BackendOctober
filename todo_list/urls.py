from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('register_page/', views.register_page, name='register_page'),
]
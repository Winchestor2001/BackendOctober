from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('task_list/', views.task_list, name='task_list'),
]
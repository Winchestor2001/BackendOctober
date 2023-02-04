from django.contrib import admin
from django.urls import path
from news.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home-page'),
    path('about/',about,name='about-page'),
    path('contact/',contact,name='contact-page'),
    path('category/',category_page,name='category-page'),
    path('register/',register_page,name='register-page'),
    path('check_username/',check_username,name='check_username'),
    
]+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

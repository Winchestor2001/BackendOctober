from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Favorite)
admin.site.register(SiteInfo)


@admin.register(FitnessProgramm)
class FitnessProgrammAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'intensity', 'gender', 'part_of_body']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title']


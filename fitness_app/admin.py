from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(FitnessProgramm)
admin.site.register(Article)
admin.site.register(Favorite)
admin.site.register(SiteInfo)

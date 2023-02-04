from django.contrib import admin
from news.models import Post,Student,ContactUs,Category, UserProfile
# Register your models here.
admin.site.site_header='Bizning website | itschool.uz'
admin.site.site_title='E-commercial website'
class StudentAdmin(admin.ModelAdmin):
    list_display=['fullname','roll_no','email','phone','fee']
    list_filter=['fullname']
    search_fields=['fullname']
    list_editable=['email','fee','phone']
admin.site.register(Post)
admin.site.register(ContactUs)
admin.site.register(Category)
admin.site.register(Student,StudentAdmin)
admin.site.register(UserProfile)

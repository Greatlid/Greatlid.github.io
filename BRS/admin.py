from django.contrib import admin
from .models import *
# Register your models here.


class UserManager(admin.ModelAdmin):
    list_display = ['username', 'password', 'userPhone', 'userEmail', 'userMajor', 'userGrade', 'userGender']
    # list_display_links = ['username']
    list_filter = ['userMajor', 'userGrade', 'userGender']
    search_fields = ['username']
    # list_editable = ['password']



admin.site.register(UserInfo, UserManager)
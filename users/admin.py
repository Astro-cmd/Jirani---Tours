from django.contrib import admin

# Register your models here.

from . models import(CustomUser,UserProfile)

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','user_id']
    list_filter = ['last_name','user_id']
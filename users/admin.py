from django.contrib import admin
from .models import User as UserModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('user','balance')
admin.site.register(UserModel,UserAdmin)

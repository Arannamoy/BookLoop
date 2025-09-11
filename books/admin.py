from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','add_date','borrow_price','added_by','category','quantity')

admin.site.register(Book,BookAdmin)
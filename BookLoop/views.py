from django.shortcuts import render
from books.models import Book as BookModel
from categories.models import Category as CategoryModel
 
def homeView(r):
    books=BookModel.objects.all().order_by('total_borrowed_time')
    categorys=CategoryModel.objects.all()
    return render(r,"index.html",{"books":books,"categorys":categorys})
from django.shortcuts import render
from books.models import Book as BookModel

def homeView(r):
    books=BookModel.objects.all()
    return render(r,"index.html",{"books":books})
from django.shortcuts import render
from .models import Book as BookModel
# Create your views here.
def getAllBook(r):
    books=BookModel.objects.all()
    return render(r,"books.html",{"books":books})

def getSpecificBook(r,id):
     book=BookModel.objects.get(pk=id)
     return render(r,'book.html',{'book':book})
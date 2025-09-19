from django.shortcuts import render
from .models import Book as BookModel
from borrow_records.models import Borrow_record as Borrow_recordModel
from datetime import datetime

# Create your views here.
# def getAllBook(r):
    # books=BookModel.objects.all()
    # return render(r,"books.html",{"books":books})

def getSpecificBook(r,id):
     book=BookModel.objects.get(pk=id)
     return render(r,'book.html',{'book':book})
def borrowBook(r,id):
    book=BookModel.objects.get(pk=id)
    Borrow_recordModel.objects.create(user=r.user,book=book,borrow_date=datetime())
    return render('borrow_record')
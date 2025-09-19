from django.shortcuts import render,redirect
from .models import Book as BookModel
from borrow_records.models import Borrow_record as Borrow_recordModel
from datetime import datetime

# Create your views here.
# def getAllBook(r):
    # books=BookModel.objects.all()
    # return render(r,"books.html",{"books":books})

def getSpecificBook(r,id):
    if r.user.is_authenticated:
        book=BookModel.objects.get(pk=id)
        return render(r,'book.html',{'book':book})
    else:
        return redirect('home')

def borrowBook(r,id):
    if r.user.is_authenticated:
        book=BookModel.objects.get(pk=id)
        Borrow_recordModel.objects.create(user=r.user,book=book,borrow_date=datetime.now())
        print(book)
        return redirect('read')
    else:
        return redirect('home')
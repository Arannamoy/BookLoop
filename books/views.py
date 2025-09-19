from django.shortcuts import render,redirect
from .models import Book as BookModel
from borrow_records.models import Borrow_record as Borrow_recordModel
from datetime import datetime

# Create your views here.
# def getAllBook(r):
    # books=BookModel.objects.all()
    # return render(r,"books.html",{"books":books})


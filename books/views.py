from django.shortcuts import render,redirect
from .models import Book as BookModel
from borrow_records.models import Borrow_record as Borrow_recordModel
from users.models import User as UserModel
from transactions.models import Transaction as TransactionModel
import datetime

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
        user=UserModel.objects.get(user=r.user)
        user.balance-=book.borrow_price
        user.save()
        TransactionModel.objects.create(user=r.user,amount=book.borrow_price,transaction_type="Debit",payment_status="Success",reference=f"TXN{r.user.id}{TransactionModel.objects.count()}")
        Borrow_recordModel.objects.create(user=r.user,book=book,borrow_date=datetime.datetime.now(),return_date=datetime.datetime.now() + datetime.timedelta(days=7),return_status="Not")
        return redirect('borrow_history')
    else:
        return redirect('login')
    


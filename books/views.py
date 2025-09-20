from django.shortcuts import render,redirect,HttpResponse
from .models import Book as BookModel
from borrow_records.models import Borrow_record as BorrowRecordModel
from users.models import User as UserModel
from transactions.models import Transaction as TransactionModel
from categories.models import Category as CategoryModel
import datetime

# Create your views here.

def getAllBook(r,slug=None):
    if slug==None:
        books=BookModel.objects.all()
    books=BookModel.objects.all()
    return render(r,"books.html",{"books":books,"categorys":CategoryModel.objects.all()})

def getSpecificBook(r,id):
        book=BookModel.objects.get(pk=id)
        return render(r,'book.html',{'book':book})
   

def borrowBook(r,id):
    if r.user.is_authenticated:
        book=BookModel.objects.get(pk=id)
        user=UserModel.objects.get(user=r.user)
        borrow = BorrowRecordModel.objects.filter(user=r.user,book=book,return_status="Not")
        if(user.balance<=book.borrow_price and user.balance<=(book.borrow_price+100)):
             return render(r,"failed_modal.html",{"message":"You do not have sufficient balance. Minimum balance must be 500."})
        if borrow:
             return render(r,"failed_modal.html",{"message":"You have already borrowed this book"})
        book.quantity-=1
        book.total_borrowed_time+=1
        book.save()
        user.balance-=book.borrow_price
        user.save()
        TransactionModel.objects.create(user=r.user,amount=book.borrow_price,transaction_type="Debit",payment_status="Success",reference=f"TXN{r.user.id}BB{TransactionModel.objects.count()}")
        BorrowRecordModel.objects.create(user=r.user,book=book,borrow_date=datetime.datetime.now(),return_date=datetime.datetime.now() + datetime.timedelta(days=7),return_status="Not")
        return redirect('borrow_history')
    else:
        return redirect('login')
    

def returnBook(r,book_id,borrow_id):
        if r.user.is_authenticated:
            book=BookModel.objects.get(pk=book_id)
            book.quantity+=1
            book.save()
            user=UserModel.objects.get(user=r.user)
            user.balance+=book.borrow_price
            user.save()
            borrow=BorrowRecordModel.objects.get(pk=borrow_id)
            borrow.return_status="Returned"
            borrow.save()
            TransactionModel.objects.create(user=r.user,amount=book.borrow_price,transaction_type="Credit",payment_status="Success",reference=f"TXN{r.user.id}RB{TransactionModel.objects.count()}")
            return redirect('borrow_history')
        else:
             return redirect('login')
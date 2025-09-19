from django.shortcuts import render,redirect
from .models import Borrow_record
# Create your views here.
# def create(request,book):
#     Borrow_record.objects.create(user=request.user,book=book)
def read(request):
    if request.user.is_authenticated:
        b =  Borrow_record.objects.filter(user = request.user)
        return render (request,'borrow_record.html',{'b':b})  
    else:
        return redirect('home')
    
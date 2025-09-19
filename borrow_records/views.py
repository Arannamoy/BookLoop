from django.shortcuts import render
from .models import Borrow_record
# Create your views here.
# def create(request,book):
#     Borrow_record.objects.create(user=request.user,book=book)
def read(request):
    b =  Borrow_record.objects.filter(user = request.user)
    print(b)
    #return render (request,'borrow_record.html',{'b':b})  
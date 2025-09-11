from django.db import models
from book.models import BookModel 
from django.contrib.auth.models import User
from CONSTANT import *
# Create your models here.


class User(models.Model):
    user=models.ForeignKey(User,related_name="user_acc",on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    contact_no=models.CharField(max_length=11,unique=True)
    borrowed_books=models.ManyToManyField(BookModel, related_name='borrowed_books', blank=True)
    gender=models.CharField(max_length=20,choices=GENDER)
    deposit_date=models.DateField(auto_now_add=True)
    balance=models.DecimalField(decimal_places=2,max_digits=12,default=0)
    dob=models.DateField()
    joining_time=models.DateTimeField(auto_now=True)
    user_image=models.ImageField(upload_to="user_image",null=True,blank=True)
    user_type=models.CharField(choices=USER_TYPE,null=True,default="ADMINISTRATIVE")
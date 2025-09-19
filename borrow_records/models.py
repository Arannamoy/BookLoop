from django.db import models
from django.contrib.auth.models import User
from books.models import Book as BookModel

# Create your models here.
class Borrow_record(models.Model):
    user = models.ForeignKey (User,related_name="user_borrow_record",on_delete=models.CASCADE)
    book = models.ManyToManyField (BookModel,null=True)
    borrow_date=models.DateTimeField(null=True)
    return_date =models.DateTimeField(null=True)
    created_at =models.DateTimeField(auto_now=True,null=True)
from django.db import models
from django.contrib.auth.models import User
from books.models import Book as BookModel
from CONSTANT import RETURN_STATUS
# Create your models here.
class Borrow_record(models.Model):
    user = models.ForeignKey (User,related_name="user_borrow_record",on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(null=True)
    return_status=models.CharField(choices=RETURN_STATUS,null=True)
    return_date =models.DateTimeField(null=True)
    created_at =models.DateTimeField(auto_now=True,null=True)
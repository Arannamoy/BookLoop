from django.db import models
from categorys.models import Category
# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True)
    author=models.CharField(max_length=150,null=True)
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    borrow_price=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    book_image=models.ImageField(upload_to="book_image",blank=True,null=True)
    added_by=models.CharField(max_length=150,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    total_borrowed_time=models.IntegerField(default=0,null=True)

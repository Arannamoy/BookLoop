from django.db import models
from django.contrib.auth.models import User
from CONSTANT import TRANSACTION_TYPE
# Create your models here.
class Transaction(models.Model):
      user=models.ForeignKey(User,related_name="user_transaction",on_delete=models.CASCADE)
      amount=models.FloatField()
      transaction_type=models.CharField(choices=TRANSACTION_TYPE)
      created_at=models.DateTimeField(auto_now=True)
      
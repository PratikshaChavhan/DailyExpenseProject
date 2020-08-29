from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=30)
    incomeDate=models.DateField()  # date format is only in 01/01/2020   and 01.01.2020 is not allowed.
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=30)
    expenseDate=models.DateField()
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


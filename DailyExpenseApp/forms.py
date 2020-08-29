from django import forms
from .models import Income,Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields="__all__"

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields="__all__"




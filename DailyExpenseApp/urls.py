from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home),
    path('addUser', v.addUser),
    path('addIncome', v.addIncome),
    path('addExpense', v.addExpense),
    path('editExpense',v.editExpense),
    path('incomeList',v.incomeList),
    path('editIncome',v.editIncome),
    path('deleteIncome',v.deleteIncome),
    
    path('expenseList',v.expenseList),
    path('editExpense',v.editExpense),
    path('deleteExpense',v.deleteExpense),


    path('userlogin',v.userlogin),
    path('userlogout',v.userlogout),

    path('editProfile',v.editProfile)

]

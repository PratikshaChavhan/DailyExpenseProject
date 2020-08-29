from django.shortcuts import render,HttpResponse,redirect
from .forms import UserForm,IncomeForm,ExpenseForm
from .models import User,Income,Expense
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    userName=request.session.get('userName')
    uid=request.session.get('UserId')
    totalIncome=0
    totalExpense=0
    incl=Income.objects.filter(user_id=uid)
    for i in incl:
        totalIncome=totalIncome + i.income
    exp=Expense.objects.filter(user_id=uid)
    for j in exp:
        totalExpense=totalExpense + j.expense
    Balance = totalIncome - totalExpense
    print("--------------------------------",totalIncome,totalExpense)

    d={'uname':userName ,'Balance':Balance}
    return render(request,'index.html',d)

def addUser(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f=UserForm
        return render(request,'form.html',{'form':f})


def addIncome(request):
    if request.method=='POST':
        d=IncomeForm(request.POST)
        d.save()
        return redirect("/")
    else:
        d=IncomeForm
        return render(request,'form.html',{'form':d})

def addExpense(request):
    if request.method=='POST':
        f=ExpenseForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f=ExpenseForm
        return render(request,'form.html',{'form':f})

def incomeList(request):
    uid=request.session.get('UserId')
    incl=Income.objects.filter(user_id=uid)
    d={'incl':incl}
    return render(request,'incomelist.html',d)

def editIncome(request):
    uid=request.session.get('userId')
    id=request.GET.get('id')
    inc=Income.objects.get(id=id)
    if request.method=='POST':
        f=IncomeForm(request.POST,instance=inc)
        f.save()
        return redirect("/incomeList")

    else:    
        f=IncomeForm(instance=inc)
        return render(request,'update.html',{'form':f})
     

def deleteIncome(request):
    id=request.GET.get('id')
    inc=Income.objects.get(id=id)
    inc.delete()
    return redirect('/incomeList')

def expenseList(request):
    uid=request.session.get('UserId')
    exp=Expense.objects.filter(user_id=uid)
    d={'exp':exp}
    return render(request,'expenselist.html',d)


def editExpense(request):
    id=request.GET.get('id')
    exp=Expense.objects.get(id=id)
    if request.method=='POST':
        f=ExpenseForm(request.POST,instance=exp)
        f.save()
        return redirect("/expenseList")

    else:    
        f=ExpenseForm(instance=exp)
        return render(request,'update.html',{'form':f})
     

def deleteExpense(request):
    id=request.GET.get('id')
    exp=Expense.objects.get(id=id)
    exp.delete()
    return redirect('/expenseList')


def userlogin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['UserId']=usr.id
            request.session['userName']=uname
            login(request,usr)
            return redirect("/")
    else:
        return render(request,"login.html")


def userlogout(request):
    logout(request)
    return redirect("/")


def editProfile(request):
    uid=request.session.get('UserId')
    u=User.objects.get(id=uid)
    f=UserForm(instance=u)
    return render(request,'form.html',{'form':f})    
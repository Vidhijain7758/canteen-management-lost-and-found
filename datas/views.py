

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from datas.forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import order,select
from .forms import LoginForm, select2,query
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min, Sum
import datetime
import matplotlib.pyplot as plt
import datetime
from matplotlib.pyplot import figure, title, bar
import numpy as np
import mpld3
from django.views.generic import UpdateView
import matplotlib
from matplotlib import cm


# Create your views here.
def start(request):
    return render(request, 'datas/start.html')


def login1(request):

    myform = LoginForm(request.POST or None)
    if myform.is_valid():
        status = request.User.last_name
        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

                return redirect("/profile")
        else:
            messages.error(request, "Error")



    return render(request, "datas/login.html", {"form": myform})


def login2(request):
    myform = LoginForm(request.POST or None)
    if myform.is_valid():
        status = request.User.last_name
        usern = myform.cleaned_data.get("username")
        passw = myform.cleaned_data.get("password")

        user = authenticate(username=usern, password=passw)
        if user:

            return redirect("/profile1")
        else:
            messages.error(request, "Error")

    return render(request, "datas/login.html", {"form": myform})

def select1(request):
    if (request.method == 'POST'):
        form1 = select2(request.POST)
        if (form1.is_valid()):

            a = form1.cleaned_data['sele']

            if(a == 'student'):
                return redirect("/login1")
            elif(a == 'cafeteria'):
                return redirect("/login2")
        else:
            messages.error(request, "Error")
    else:
        form1 = select2()
        return render(request, 'datas/select.html', {'form': form1})

    args = {'user': request.user}
    return render(request, 'datas/select.html', args)


def register(request):
    if (request.method == 'POST'):
        form = CustomUserCreationForm(request.POST)
        if (form.is_valid()):
            form.save()


            return redirect('/login')
        else:
            messages.error(request, "Error")
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, 'datas/signup.html', args)


def profile1(request):
    if (request.user.username):
        a = str(request.user.last_name)
        if (a == 'student'):
            return render(request, 'datas/profile.html')
        elif(a== 'cafeteria'):
            return render(request,'datas/profile1.html')

def profile(request):
    args = {'user': request.user}
    return render(request,'datas/profile.html',args)

def home(request):

            return render(request,'datas/home.html')
            # return redirect('/result')




def home1(request):
            return render(request,'datas/home1.html')
            # return redirect('/result')

def home2(request):
    return render(request,'datas/home2.html')

def home3(request):
    return render(request,'datas/home3.html')

def check(request):

    return render(request, 'datas/check.html')

def menu(request):
    return render(request,'datas/menu.html')

def order(request):

        products = Order.objects.all()
        return render(request, 'order.html', {'orders': products})

def helper(output):
    monthly =0.0
    a = 0.0
    b =0.0
    for i in output:
        a  = a + i.sam_earned
        b = b + i.sam_avaliable
    monthly = (a/b)
    return monthly

def helper2(output):
    monthly = 0.0
    a = 0.0
    b = 0.0
    for i in output:
        a = a + i.sam_earned
        b = b + i.sam_avaliable
    monthly =   (a / b)
    return monthly
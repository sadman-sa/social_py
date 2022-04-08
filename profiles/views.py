from django.shortcuts import render, redirect
from django.http import HttpResponse
from profiles.models import Record
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

from .forms import CreatUserForm

from django.contrib.auth import authenticate, login, logout
from .decorator import  unauthenticated_user
from django.contrib.auth.decorators import login_required



@unauthenticated_user
def base(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "user has been registered")
            return redirect('../form/')
        else:
            messages.success(request, "You typed something wrong please try again")
    context = {'form':form}
    return render(request, 'form.html' , context)

@login_required(login_url='../form/')
def logoutUser(request):
    logout(request)
    return redirect('../form/')

@unauthenticated_user
def form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return render(request, 'home.html')
    return render(request, 'login.html')
    


from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Record
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='../form/')
def user_list(request):
    all_u = User.objects.all()
    return render(request, 'user_list.html', {'list_u' : all_u})



@login_required(login_url='../form/')
def own_profile(request, pk):
    user = User.objects.get(pk=pk) 
    return render(request, 'own_profile.html' , {'user': user, 'pk':pk})
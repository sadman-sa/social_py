from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ThoughT, Comment
from django.contrib import messages 


@login_required(login_url='../form/')
def home(request):
     all_thought = ThoughT.objects.all()
     if request.method == 'POST':
         thought = request.POST['thought']
         user = request.user
         ins = ThoughT(thoughts=thought, user=user)
         ins.save()
         return redirect('../home/')
     else:
         messages.success(request, "something went wrong please try again")

     return render(request,'home.html', {'list_thought' : all_thought})
 
def like_post(request):
     user = request.user
     if request.method == 'POST':
         post_id = request.POST.get('post_id')
         post_obj = ThoughT.objects.get(id=post_id)

         if user in post_obj.liked.all():
             post_obj.liked.remove(user) 
         else:
             post_obj.liked.add(user)
     return redirect('../home/')

def comment_post(request):
     user = request.user
     if request.method == 'POST':
         comment = request.POST['comment_input']
         post_id = request.POST.get('post_id')
         post_obj = ThoughT.objects.get(id=post_id)

         ins = Comment(user = user, comment = comment, container_post = post_obj )
         ins.save()

     return redirect('../home/')
from django.shortcuts import render, redirect
from . models import Message
from django.contrib.auth.models import User


def message(request, mpk):
    sender = request.user
    recievere = User.objects.get(pk=mpk)
    msg = Message.objects.all()
    if request.method == 'POST':
         msg = request.POST['message']
         ins = Message(message_sender=sender, message_ricevere=recievere, sent_message=msg)
         ins.save()  
    return render(request, 'message.html', {'receivere':recievere, 'sender':sender , 'msg':msg})


def chat_app(request):
    mssg = Message.objects.all()
    list = []
    for msg in mssg:
      if msg.message_sender not in list:
          if msg.message_ricevere == request.user:
                list.append(msg.message_sender)
    print(list)
    return render(request, 'chat.html', {'msg':list})
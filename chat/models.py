from django.db import models
from django.contrib.auth.models import User 


class Message(models.Model):
    message_sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='msg_s')
    sent_message = models.CharField(max_length=500, blank=True)
    message_ricevere  = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE, related_name="msg_r")
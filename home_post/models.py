from django.db import models
from django.contrib.auth.models import User 


class ThoughT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')
    thoughts = models.CharField(max_length=500)
    liked = models.ManyToManyField(User, blank=True, related_name='liked')



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, blank=True)
    container_post = models.ForeignKey(ThoughT,null=True, blank=True, on_delete=models.CASCADE, related_name="comments")
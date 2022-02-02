
from email.policy import default
from django.db import models
from django.conf import settings




# Create your models here.


class Tweet(models.Model):
   # Maps to postgresql data
   id = models.TextField(primary_key=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   content = models.TextField(blank=True,null=True)
   updated = models.DateTimeField(auto_now=True)
   timestamp = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.content


from email.policy import default
from django.db import models
from django.conf import settings




# Create your models here.
class User(models.Model):
   content = models.TextField(blank=False,null=False)
class Tweet(models.Model):
   # Maps to postgresql data
   id = models.AutoField(primary_key=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL,null=False,blank=True,on_delete=models.CASCADE)
   content = models.TextField(blank=True,null=True)
   timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)

   def __str__(self):
      return self.user

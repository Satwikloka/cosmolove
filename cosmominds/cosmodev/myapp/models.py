

from django.conf import settings

from django.db import models
from .validators import validate_content
from django.urls import reverse



# Create your models here.



class Tweet(models.Model):
   # Maps to postgresql data

   id = models.TextField(primary_key=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   content = models.TextField(max_length =240,validators=[validate_content])
   updated = models.DateTimeField(auto_now=True)
   timestamp = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return (self.content)

   def get_absolute_url(self):
       return reverse("tweet_detail", kwargs={"pk": self.pk})
   

   #

class User(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

   def __str__(self):
      return self.user

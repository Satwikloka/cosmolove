

from django.conf import settings
from django.core.exceptions import ValidationError

from django.db import models
from django.urls import reverse

from .validators import validate_content



# Create your models here.



class Tweet(models.Model):
   # Maps to postgresql data

   sid = models.AutoField(primary_key=True,null=False)
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   content = models.TextField(max_length =240,validators=[validate_content])
   updated = models.DateTimeField(auto_now=True)
   timestamp = models.DateTimeField(auto_now_add=True)   
   def __str__(self):
      return (self.content)

   def get_absolute_url(self):
       return reverse ("tweet:detail", kwargs={"pk": self.pk})
   

   #



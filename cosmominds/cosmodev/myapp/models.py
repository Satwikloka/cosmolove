from django.db import models




# Create your models here.
class User(models.Model):
   content = models.TextField(blank=False,null=False)
class Tweet(models.Model):
   # Maps to postgresql data
   # id  models.AutoField(primary_key=True) 
   content = models.TextField(blank=True,null=True)

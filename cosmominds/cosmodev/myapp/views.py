from django.contrib.messages.api import info
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .forms import TweetForm
from rest_framework.parsers import JSONParser






import random

from .models import Tweet 


# Create your views here.

def cs(request):

    if request.method == 'POST':
        username = request.POST.get('username',False)
        password = request.POST.get('password',False)
        user = User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request, "Your account created successfully for Basic use of cosmominds.")
        return redirect('feeds.html',context ={})
    else:
        return render(request,'cs.html')




def tweet_create_view(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()
    return render(request,'feeds.html',context={})

    
def tweet_list_view(request,*args, **kwargs):
    qs=Tweet.objects.all()
    tweets_list=[{"id":x.id,"content":x.content,"likes":random.randint(0,999)}for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request,tweet_id):
    """
    REST API view
    consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    if request.method == 'GET':
        data = {
            "id":tweet_id,
        }
        status = 200
        try:
            obj = Tweet.objects.get(id=tweet_id)
            data['content'] = obj.content
        except:
            data['message'] = "Not found"
            status = 400
        return JsonResponse(data,status = status) #json.dumps

        
    

        







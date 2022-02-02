
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import TweetForm





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
    return render(request,'create_view.html',context={})

    
def tweet_list_view(request):
    queryset=Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list":queryset
    }
    return render(request,"list_view.html",context)

#Retrieve
def tweet_detail_view(request,id):
    """
    REST API view
    consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {
        "object":obj
    }
    return render(request,"detail_view.html", context)

        
    

        







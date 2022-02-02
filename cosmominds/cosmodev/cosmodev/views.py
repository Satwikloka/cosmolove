from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages



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
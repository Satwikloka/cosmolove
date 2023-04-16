from audioop import reverse
from sre_constants import SUCCESS
from .mixins import FormUserNeededMixin,UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView,RedirectView
from .forms import TweetModelForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from chartjs.views.lines import BaseLineChartView
from.models import Tweet






from .models import Tweet 


# Create your views here.

class BusinessPageView(TemplateView):
    template_name='businesscard.html'
class InterfacePageView(TemplateView):
    template_name='interface.html'
class MainPageView(TemplateView):
    template_name='mainpage.html'
class TweetCreateView(FormUserNeededMixin,CreateView):
    #queryset =Tweet.objects.all()
    form_class = TweetModelForm
    
    template_name = 'tweetlist.html'

user = get_user_model

class UserDetailView(DetailView):
    queryset=User.objects
   
        

    
    #success_url: reverse_lazy("tweet:create")
    #login_url = '/admin/'


  

    

    

    #
# update
class TweetUpdateView(UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'update_view.html'
   # success_url = "tweet/"
    





#retrieve
class TweetDetailView(DetailView):
    #template_name = "detail_view.html"
    queryset = Tweet.objects.all()
    #success_url = reverse_lazy("tweet:detail")

    #def get_object(self):
    #    print(self.kwargs)
     #   pk = self.kwargs['pk']
    #    print(pk)
    #    return Tweet.objects.get(id=pk)


class TweetListView(ListView):
    template_name = "tweetlist.html" 
    #queryset = Tweet.objects.all()
    def get_queryset(self,*args,**kwargs):
        queryset = Tweet.objects.all()
        
        query = self.request.GET.get("q",None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query)|
                Q(user__username_icontains=query)
                )
        return queryset

    def get_context_data(self,*args ,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:list')
        return context

#delete view
class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = "delete_confirm.html"
    success_url = reverse_lazy('tweet:list')
#



#
    
#def tweet_list_view(request):
 #   queryset=Tweet.objects.all()
  #  print(queryset)
 #   for obj in queryset:
  #      print(obj.content)
 #   context = {
  #      "object_list":queryset
  #  }
  #  return render(request,"list_view.html",context)

#Retrieve
#
class EditorChartView(TemplateView):
    template_name = 'line_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Tweet.objects.all()
        return context
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import RedirectView


from .views import( TweetListView,TweetDetailView,TweetCreateView,TweetUpdateView,TweetDeleteView,UserDetailView,RedirectView,MainPageView,BusinessPageView,InterfacePageView)

app_name='tweet'
urlpatterns = [
    path('interface',InterfacePageView.as_view(),name='interface'),
    path('business',BusinessPageView.as_view(),name='business'),
    path('login',MainPageView.as_view(),name='login'),
    path('list',TweetListView.as_view(),name='list'),
    path('create',TweetCreateView.as_view(),name='create'),
    path('<pk>/edit',TweetUpdateView.as_view(),name='update'),
    path('<pk>/delete',TweetDeleteView.as_view(),name='delete'),
    path('<pk>',UserDetailView.as_view(),name='id'),
    

    path('<pk>',TweetDetailView.as_view(),name='detail'),
    
    



    
    
] 
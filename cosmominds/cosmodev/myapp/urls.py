from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from .views import( TweetListView,TweetDetailView,TweetCreateView,TweetUpdateView,TweetDeleteView,UserDetailView)

app_name='tweet'
urlpatterns = [
    path('',RedirectView.as_view(url="/")),
    
    path('list',TweetListView.as_view(),name='list'),
    path('create',TweetCreateView.as_view(),name='create'),
    path('<pk>/edit',TweetUpdateView.as_view(),name='update'),
    path('<pk>/delete',TweetDeleteView.as_view(),name='delete'),
    path('<pk>',UserDetailView.as_view(),name='id'),


    path('<pk>',TweetDetailView.as_view(),name='detail'),
    
    



    
    
] 
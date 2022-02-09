from django.contrib import admin
from django.urls import path,re_path

from .views import( TweetListView,TweetDetailView,TweetCreateView,TweetUpdateView,TweetDeleteView)


urlpatterns = [
    path('admin/',admin.site.urls),
    path('list',TweetListView.as_view(),name='list'),
    path('<create>',TweetCreateView.as_view(),name='create'),
    path('<pk>/edit',TweetUpdateView.as_view(),name='update'),
    path('<pk>/delete',TweetDeleteView.as_view(),name='delete'),


    path('<pk>',TweetDetailView.as_view(),name='detail'),
    
    



    
    
]
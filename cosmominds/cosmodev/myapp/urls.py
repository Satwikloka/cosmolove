from django.contrib import admin
from django.urls import path,re_path
from .views import tweet_list_view,tweet_create_view,tweet_detail_view


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',tweet_list_view,name='list'),
    path('',tweet_create_view,name='create'), 
    path('',tweet_detail_view,name='detail'),
    
    



    
    
]
from django.contrib import admin
from django.urls import path,re_path #url()
from .import views 


urlpatterns = [
    path('admin/',admin.site.urls),
    path('register',views.cs,name='signup'),
    path('feedview',views.tweet_detail_view, name='feedview'),
    path('feedviewer',views.tweet_list_view, name='feedviewer'),
    path('create-tweet',views.tweet_create_view,name='feeds'),
    



    
    
]
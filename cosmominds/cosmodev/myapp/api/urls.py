from django.contrib import admin
from django.urls import path,re_path
from rest_framework.views import APIView

from .views import (
    TweetListAPIView,TweetCreateAPIView,
)


urlpatterns = [

    path('', TweetListAPIView.as_view(),name='list'),

    path('create',TweetCreateAPIView.as_view(),name='create'),
    
    



    
    
]
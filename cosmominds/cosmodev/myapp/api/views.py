from django.conf import settings
from requests import request
from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from ..models import Tweet
from.serializers import TweetModelSerializer
from rest_framework.decorators import APIView
from django.contrib.auth import get_user_model 



class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

    

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    queryset=Tweet.objects.all()
    def get_queryset(self,*args,**kwargs):
        queryset = Tweet.objects.all().order_by("-timestamp")
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query)|
                Q(user__username=query)
                )
        return queryset
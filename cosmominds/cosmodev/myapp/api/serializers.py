
from datetime import datetime, date, time, timezone
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince


from ..models import Tweet
user = get_user_model()
class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = user
        fields = [
            'username', 
            'first_name',
            'last_name',
            'follower_count',
        ]
    def get_follower_count(self, obj):
        return 0

class TweetModelSerializer(serializers.ModelSerializer):
    user=UserDisplaySerializer(serializers.ModelSerializer)
    
    timestamp = serializers.SerializerMethodField
    
    class Meta:
        model = Tweet
        fields =[
            'user',
            'content',
            'timestamp',
            
            
            
            
        ]





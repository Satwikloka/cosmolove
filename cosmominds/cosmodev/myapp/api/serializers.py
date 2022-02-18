from rest_framework import serializers
from django.contrib.auth import get_user_model


from ..models import Tweet
User = get_user_model()
class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
        ]
    def get_follower_count(self, obj):
        return 0

class TweetModelSerializer(serializers.ModelSerializer):
    user=UserDisplaySerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields =[
            'user',
            'content',
            'timestamp',
        ]





from django.db.models import Tweet

from django.contrib.auth.models import User
from rest_framework import  serializers




# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'user'
            'content'
            

        ]
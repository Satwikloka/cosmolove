from unittest.util import _MAX_LENGTH
from django import forms

from .models import Tweet

MAX_TWEET_LENGTH = 240

class TweetModelForm(forms.ModelForm):
    
    
    class Meta:
        model = Tweet
        fields = [
             #'user',
            'content'
            ]
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This Ideation is too long")
        return content



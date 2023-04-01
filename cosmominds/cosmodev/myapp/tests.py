from django.contrib.auth import get_user_model
from django.urls import reverse



from django.test import TestCase

# Create your tests here.
 
from .models import Tweet

user = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = user.objects.create(username ='admin ')
    def test_tweet_item(self):
        data = Tweet.objects.create(
                user=user.objects.first(),
                content='Some random content'   
        )
        self.assertTrue(data.content=="Some random content")
        self.assertTrue(data.user==7)
        #self.assertEqual(obj.id,1)
        absolute_url = reverse("tweet:detail",kwargs={"pk":7})
        self.assertEqual(data.get_absolute_url(),absolute_url)
    def test_tweet_url(self):
        obj = Tweet.objects.create(
                user=user.objects.first(),
                content='Some random content' 
                )
        absolute_url = reverse("tweet:detail",kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(),absolute_url)



# Create your tests here.

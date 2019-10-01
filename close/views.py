from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from django.views.generic import View
from rest_framework.views import APIView
from allauth.socialaccount import views
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer
from allauth.socialaccount.models import SocialApp
import tweepy

from tweepy.auth import OAuthHandler
from rest_framework.response import Response


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class TwitterConnect(SocialConnectView):


    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter


class HomeView(APIView):
    def get(self, request):
        return Response("hello world")


consumer_key = '0PJ6vzF0y3ZOjCw876u77TLd3'
consumer_secret = 'tqle4sa9upfaZgXGLfPoHD96G7oZ4VkKUrLc4klnj6fp0UgC8z'
access_token = '837975466183118848-oZUdzO7WgKPnOEM4G0YjhZjc4LA7j0L'
access_token_secret = 'ijUa6AiEpzZO3Dtu7CcCuesCORjFGwgQGgeExlpY9cdgD'


class home_timeline(APIView):
    def get(self, request):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()

        give_data = []
        for tweets in public_tweets:
            data = {
                "text": tweets.text,
                "user": tweets.user.name
            }
            give_data.append(data)

        return Response({"data": give_data, "message": "success", "requestStatus": 0},
                        status=400)


class usercredential(APIView):
    def get(self, request):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        user2 = api.get_user("PraveenJs")

        data = {
            "name": user2.name,
            "description": user2.description,
            "location": user2.location
        }
        return Response({"data": data, "message": "Success", "requestStatus": 0},
                        status=200)


class mention(APIView):
    def get(self, request):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        tweets = api.mentions_timeline()
        give_data = []
        for tweet in tweets:
            data = {
                "mentions": tweet.text
            }
            give_data.append(data)

        return Response({"data": give_data, "message": "success", "requestStatus": 0},
                        status=200)


class follower(APIView):
    def get(self,request):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        user =  api.get_user("PraveenJs")
        give_data = []
        user2 =user.followers()
        for foll in user2:
            data = {
                "followers" : foll.name
            }
            give_data.append(data)

        return Response({"data": give_data, "message": "success", "requestStatus": 0},
                        status=200)




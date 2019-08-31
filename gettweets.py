#! /usr/local/bin/python3
import tweepy
import credentialstwitter

auth = tweepy.OAuthHandler(credentialstwitter.CONSUMER_KEY, credentialstwitter.CONSUMER_SECRET)
auth.set_access_token(credentialstwitter.ACCESS_TOKEN, credentialstwitter.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

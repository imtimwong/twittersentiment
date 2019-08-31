#! /usr/local/bin/python3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json

import credentialstwitter

class authenticateTwitterClass():
    """
	reads from credentialstwitter file that contains the keys and access tokens
	"""

    def authenticateTwitter(self):
        auth = OAuthHandler(credentialstwitter.CONSUMER_KEY, credentialstwitter.CONSUMER_SECRET)
        auth.set_access_token(credentialstwitter.ACCESS_TOKEN, credentialstwitter.ACCESS_TOKEN_SECRET)

        return auth

# # # Streamer
class TwitterStreamer():
    """
    To stream tweets live
    """
    def __init__(self):
        self.tweetauth = authenticateTwitterClass() #create an object of the class(constructor)


    def stream_tweets(self, fetched_tweets_filename, topics):

        listener = thestreamListener(fetched_tweets_filename)
        auth=self.tweetauth.authenticateTwitter() #to call the function inside the class authenticateTwitterClass()
        streamit = Stream(auth, listener)

        streamit.filter(track=topics)


# # # # Stream listener
class thestreamListener(StreamListener):
    """
    To extract data from json and pass it into load into db class
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, ori_raw_data):

        try:

            data = json.loads(ori_raw_data)

            # Extract values from json raw data
            #tweet_topics=topics[0],topics[1]
            tweet_topics=topics
            user_id = data['user']['id']
            user_name = data['user']['name']
            twitter_user_name = data['user']['screen_name']
            created_at = data['created_at']
            tweet = data['text']

            #print(data)
            #if 'extended_tweet' in data and 'RT @' not in data['extended_tweet']['full_text'].encode('utf-8'):
            if 'retweeted_status' in data :#and 'RT @' not in data.extended_tweet.['full_text']:


                #print("its a retweet",twitter_user_name)
                retweetstatus_user = data['retweeted_status']['user']['id']
                retweetstatus_name = data['retweeted_status']['user']['name']
                #print(data)
                #print(data['extended_tweet'])


            else:
                #print("its not a retweet")
                #print(data['text'])
                #print(data['extended_tweet']['full_text'])
                retweetstatus_user = ""
                retweetstatus_name = ""

            print(tweet_topics,"§",user_id,"§",twitter_user_name,"§",user_name,"§",tweet,"§",retweetstatus_user
                  ,"§",retweetstatus_name,"§",created_at,)
            #datajson=tweet_topics,user_id,twitter_user_name,user_name,tweet,retweetstatus_user,retweetstatus_name,created_at
            #print(datajson)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(str(tweet_topics)+"§"+str(user_id)+"§"+str(twitter_user_name)+"§"+str(user_name)+"§"+str(tweet)+"§"+str(retweetstatus_user)+"§"+str(retweetstatus_name)+"§"+str(created_at)+"\n")
            return True

            # Load it into a table in db
            # load_into_db(topics, user_id, twitter_user_name, user_name, tweet, retweetstatus_user,
            #                       retweetstatus_name, created_at)

        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True




    def on_error(self, status):
        if status == 420:
        #Return false to stop streaming when stream limit is reached
            return False
        print(status)




if __name__ == '__main__':

    topics = ["Taylor Swift", "Lover"]
    fetched_tweets_filename = "tweets.txt"

    api = API(wait_on_rate_limit_notify=True)

    #auth = authenticateTwitterClass().authenticateTwitter()

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, topics)





#! /usr/bin/python3.7

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import tweepy
 
import credentialstwitter
 
# # # # TWITTER STREAMER # # # #
# class TwitterStreamer():
#     """
#     Class for streaming and processing live tweets.
#     """
#     def __init__(self):
#         pass

#     def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
#         # This handles Twitter authetification and the connection to Twitter Streaming API
#         listener = StdOutListener(fetched_tweets_filename)
#         auth = OAuthHandler(credentialstwitter.CONSUMER_KEY, credentialstwitter.CONSUMER_SECRET)
#         auth.set_access_token(credentialstwitter.ACCESS_TOKEN, credentialstwitter.ACCESS_TOKEN_SECRET)
#         stream = Stream(auth, listener)

#         # This line filter Twitter Streams to capture data by the keywords: 
#         stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    # def __init__(self, fetched_tweets_filename):
    #     self.fetched_tweets_filename = fetched_tweets_filename

    # def on_data(self, data):
    #     try:
    #         print(data)
    #         with open(self.fetched_tweets_filename, 'a') as tf:
    #             tf.write(data)
    #         return True
    #     except BaseException as e:
    #         print("Error on_data %s" % str(e))
    #     return True

    def on_data(self, data):
    	print(data)
    	return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
   listener = StdOutListener()
   auth = OAuthHandler(credentialstwitter.CONSUMER_KEY, credentialstwitter.CONSUMER_SECRET)
   auth.set_access_token(credentialstwitter.ACCESS_TOKEN, credentialstwitter.ACCESS_TOKEN_SECRET)
   stream = Stream(auth, listener)

   stream.filter(track=['donald trump'])

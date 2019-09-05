#! /usr/local/bin/python3.7

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json
import psycopg2
import postgrescredentials

import credentialstwitter

class authenticateTwitterClass():
    """
	reads from credentialstwitter file that contains the keys and access tokens.
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

        streamit.filter(languages=["en"],track=[topics])


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

            user_id = data['user']['id']
            user_name = data['user']['name']
            twitter_user_name = data['user']['screen_name']
            created_at = data['created_at']
            tweet = data['text']

            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(str(data))
                # tf.write(str(topics)+"§"+str(user_id)+"§"+str(twitter_user_name)+"§"+str(user_name)+"§"+str(tweet)+"§"+str(created_at)+"\n")
            #return True

            # Load it into a table in db
            # load_into_db(topics, user_id, twitter_user_name, user_name, tweet, created_at)

            loadDb = load_into_db()
            loadDb.load_tweets(topics, user_id, twitter_user_name, user_name, tweet, created_at)


        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True




    def on_error(self, status):
        if status == 420:
        #Return false to stop streaming when stream limit is reached
            return False
        print(status)

class load_into_db():

    def load_tweets(self,topics, user_id, twitter_user_name, user_name, tweet, created_at):

        try:
            #reads from postgresl credentials file to connect to db
            connection = psycopg2.connect(user=postgrescredentials.user,
                                          password=postgrescredentials.password,
                                          host=postgrescredentials.host,
                                          port=postgrescredentials.port,
                                          database=postgrescredentials.database)
            cursor = connection.cursor()


            cursor.execute("INSERT INTO TWITTER_USR (USR_ID,USR_NM,TWITTER_USR_NM) VALUES (%s,%s,%s) ON CONFLICT(USR_ID) DO NOTHING;",(user_id,user_name,twitter_user_name))

            cursor.execute("INSERT INTO TWEETS (USR_ID,TOPICS,TWEET_TEXT,CREATED_AT) VALUES (%s,%s,%s,%s);",(user_id,topics,tweet,created_at))

            connection.commit()

            count = cursor.rowcount
            print(count, "Record inserted successfully into table")


        except (Exception, psycopg2.Error) as error:
            print("Failed to insert into table", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")




if __name__ == '__main__':

    #topics = ["Taylor Swift", "Lover"]
    topics = "Taylor Swift"
    fetched_tweets_filename = "tweets.txt"

    api = API(wait_on_rate_limit_notify=True)

    #auth = authenticateTwitterClass().authenticateTwitter()

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, topics)





#! /usr/local/bin/python3.7

#import for db connection
import psycopg2
import postgrescredentials

#import for ORM
import sqlalchemy as db

#import
import numpy as np
import pandas as pd

import re



sqlengine = db.create_engine('postgres+psycopg2://%s:%s@%s:%s/%s'%(postgrescredentials.user,postgrescredentials.password,postgrescredentials.host,postgrescredentials.port,postgrescredentials.database))

con = sqlengine.connect()

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html

#s = db.select([tweets])
#result = con.execute(s)
#result = con.execute("SELECT TWEET_TEXT FROM TWEETS")
s="SELECT * FROM TWEETS;"

df = pd.read_sql(s,con, index_col="tweet_id")

#put everythin in lowercase
df['tweet_text'] = df['tweet_text'].str.lower()
#Replace rt indicating that was a retweet_text
df['tweet_text'] = df['tweet_text'].str.replace('rt', '')
#Replace occurences of mentioning @UserNames
df['tweet_text'] = df['tweet_text'].replace(r'@\w+', '', regex=True)
#Replace links contained in the tweet_text
df['tweet_text'] = df['tweet_text'].replace(r'http\S+', '', regex=True)
df['tweet_text'] = df['tweet_text'].replace(r'www.[^ ]+', '', regex=True)
#remove next line \n
df['tweet_text'] = df['tweet_text'].replace('\n','', regex=True)
#remove numbers
df['tweet_text'] = df['tweet_text'].replace(r'[0-9]+', '', regex=True)
#replace special characters and puntuation marks
df['tweet_text'] = df['tweet_text'].replace(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', '', regex=True)



#print(df.head(10))
#print(df.head(10))
#print(df['tweet_text'].str.replace('RT', ''))

# cleanedtweet = str(df['tweet_text'])
#
# cleanedtweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanedtweet).split())
#
# #aiya just copy fucj
# #def clean_tweet(self, cleaned=df['tweet_text']):
# #    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", df['tweet_text']).split())
#
# #print(df['tweet_text'])
# print(cleanedtweet)
# df['tweet_text']=cleanedtweet
#
print(df['tweet_text'].iloc[2])

# for row in df:
#     cleanedtweet = str(df['tweet_text'])
# 
#     cleanedtweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanedtweet).split())
#     df['tweet_text'] = cleanedtweet
# 
#     print(df['tweet_text'])

# for row in result:
#     print(row[tweets.c.tweet_text])
#
# result.close()



#if __name__ == '__main__':
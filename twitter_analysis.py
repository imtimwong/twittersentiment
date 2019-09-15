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

import nltk
from nltk.corpus import (stopwords)







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
print(df['tweet_text'].iloc[7])

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



#for s in sentences:
#    print(" ".join(text_processor.pre_process_doc(s)))

#https://stackoverflow.com/questions/29523254/python-remove-stop-words-from-pandas-dataframe
stop_words_eng = stopwords.words('english')
#df['tweet_text'] = df['tweet_text'].str.lower()
#lamda - hidden function
#apply is used to apply the lamda function on one column
#split the tweet using space in x.split() then check for if its not a stop word then join it together again with space
df['tweet_text'] = df['tweet_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words_eng)]))

filtered_sentence = [w for w in df['tweet_text'] if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


print(df['tweet_text'].iloc[7])

#if __name__ == '__main__':
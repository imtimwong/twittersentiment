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
#need to manuall download 'punkt' before using this : nltk.download('punkt')
from nltk.corpus import (stopwords)

#for correcting elongated words
from nltk.tokenize import word_tokenize

#for os intraction
import os






sqlengine = db.create_engine('postgres+psycopg2://%s:%s@%s:%s/%s'%(postgrescredentials.user,postgrescredentials.password,postgrescredentials.host,postgrescredentials.port,postgrescredentials.database))

con = sqlengine.connect()

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html

#s = db.select([tweets])
#result = con.execute(s)
#result = con.execute("SELECT TWEET_TEXT FROM TWEETS")

#put all preprocessing into one class later
s="SELECT * FROM TWEETS;"


df = pd.read_sql(s,con, index_col="tweet_id")


#print(df['tweet_text'])
#print(df.tweet_text.to_string(index=False, header=False))

#change tweets into lowercase
df['tweet_text'] = df['tweet_text'].str.lower()
#Removing RT retweet term
df['tweet_text'] = df['tweet_text'].str.replace('rt', '')
#Removing usernames
df['tweet_text'] = df['tweet_text'].replace(r'@\w+', '', regex=True)
#Removing url links
df['tweet_text'] = df['tweet_text'].replace(r'http\S+', '', regex=True)
df['tweet_text'] = df['tweet_text'].replace(r'www.[^ ]+', '', regex=True)
#remove next line \n
df['tweet_text'] = df['tweet_text'].replace('\n',' ', regex=True)
#remove numbers
df['tweet_text'] = df['tweet_text'].replace(r'[0-9]+', '', regex=True)
#removing special characters
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
print(df['tweet_text'].iloc[50])

# for row in df:
#cleanedtweet = str(df['tweet_text'])
# 
#     cleanedtweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanedtweet).split())
#     df['tweet_text'] = cleanedtweet

#df['tweet_text'] = df['tweet_text'].apply(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanedtweet).split()))
#df['tweet_text'] = df['tweet_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words_eng)]))
# 
#     print(df['tweet_text'])

# for row in result:
#     print(row[tweets.c.tweet_text])
#
# result.close()



#for s in sentences:
#    print(" ".join(text_processor.pre_process_doc(s)))

#https://stackoverflow.com/questions/29523254/python-remove-stop-words-from-pandas-dataframe
#removing stop words such as "the,a,in,an"
stop_words_eng = stopwords.words('english')
#df['tweet_text'] = df['tweet_text'].str.lower()
#lamda - hidden function
#apply is used to apply the lamda function on one column
#split the tweet using space in x.split() then check for if its not a stop word then join it together again with space
#and move on to the next word of the tweet


df['tweet_text'] = df['tweet_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words_eng)]))
print(df['tweet_text'].iloc[50])

tweet = word_tokenize(str(df['tweet_text'].iloc[50]))

print(tweet)

df['tweet_text'] = df['tweet_text'].apply(word_tokenize)

#filtered_sentence = [w for w in df['tweet_text'] if not w in stop_words]

#filtered_sentence = []

# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)

#print(df['tweet_text'])

print(df['tweet_text'].iloc[50])


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

file = os.getcwd()


print(file)
#text = df.tweet_text
#print(textdf)
text = df.tweet_text.to_string( index=False, header=False)
# this one ABOVEeee coorect
#print(text)

#text = pd.Series([t for t in df.tweet_text]).str.cat(sep=' ')
#text = pd.Series([str(t) for t in df.tweet_text]).str.cat(sep=' \',')

#wordcloud2 = WordCloud().generate(' '.join(text2['Crime Type']))

#text = ' '.join(str(w) for w in df.tweet_text)


wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    background_color = 'black',
    stopwords = STOPWORDS
).generate(text)
#generate(' '.join(str(df['tweet_text']))
fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)

wcpath=file+"/first_review.png"

print(wcpath)

wordcloud.to_file(wcpath)
plt.show()

#if __name__ == '__main__':

#word_cloud(pd.Series([t for t in tweet_table.tweet]).str.cat(sep=' '))
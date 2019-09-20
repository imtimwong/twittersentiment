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


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from textblob import TextBlob


class extractDB():

    def sqlconnect(self):

        sqlengine = db.create_engine('postgres+psycopg2://%s:%s@%s:%s/%s'%(postgrescredentials.user,postgrescredentials.password,postgrescredentials.host,postgrescredentials.port,postgrescredentials.database))

        con = sqlengine.connect()

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html

#s = db.select([tweets])
#result = con.execute(s)
#result = con.execute("SELECT TWEET_TEXT FROM TWEETS")

#put all preprocessing into one class later
        s="SELECT * FROM TWEETS;"


        df = pd.read_sql(s,con, index_col="tweet_id")


        return df


#print(df['tweet_text'])
#print(df.tweet_text.to_string(index=False, header=False))


class data_preparation():

    def preprocessing(self,df):

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
        print(df['tweet_text'].iloc[60])

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
        return df


    def remove_stopwords(self,df):

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
        print(df['tweet_text'].iloc[60])

        return df






        #https://towardsdatascience.com/the-real-world-as-seen-on-twitter-sentiment-analysis-part-one-5ac2d06b63fb
        #tweet = word_tokenize(str(df['tweet_text'].iloc[50])) this works too

        #print(tweet)

        #df['tweet_text'] = df['tweet_text'].apply(word_tokenize) this works

        #filtered_sentence = [w for w in df['tweet_text'] if not w in stop_words]

        #filtered_sentence = []

        # for w in word_tokens:
        #     if w not in stop_words:
        #         filtered_sentence.append(w)

        #print(df['tweet_text'])



        print(df['tweet_text'].iloc[50])

        #print(df['tweet_text'])


        #
        #
        # textanalysis = df.tweet_text.to_string( index=False, header=False)
        #






class wordcloud():

    def wordclouddraw(self,df,sent):



        file = os.getcwd()


        print(file)
        #text = df.tweet_text
        #print(textdf)

        if sent == 'positive':

            #sentiment_value = 1
            text_filtered_sentiment = df['sentiment'] == 1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/pos_tweets.png"

        elif sent == 'negative':
            #sentiment_value = -1
            text_filtered_sentiment = df['sentiment'] == -1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/neg_tweets.png"

        else:

            text = df.tweet_text.to_string( index=False, header=False)
            filename = "/all_tweets.png"

        # sentiment_value = 1
        # is_positive = df['sentiment'] == 1
        # is_positive2 = df[is_positive]
        # text = is_positive2.tweet_text.to_string(index=False, header=False)
        # filename = "/pos_tweets.png"

        #print(is_positive2)


        #print(text_filtered_sentiment)

        #text = text_filtered_sentiment.tweet_text.to_string( index=False, header=False)
        # this one ABOVEeee coorect
        #print(text)

        #text2 = pd.Series([t for t in df.tweet_text]).str.cat(sep=' ')
        #text = pd.Series([str(t) for t in df.tweet_text]).str.cat(sep=' \',')

        #wordcloud2 = WordCloud().generate(' '.join(text2['Crime Type']))

        #text = ' '.join(str(w) for w in df.tweet_text)

        #print(text)
        #print(text2)


        wordcloud = WordCloud(
            width = 3000,
            height = 2000,
            background_color = 'black',
            #stopwords = STOPWORDS
            stopwords=['taylor swift']
        ).generate(text)
        #generate(' '.join(str(df['tweet_text']))
        fig = plt.figure(
            figsize = (40, 30),
            facecolor = 'k',
            edgecolor = 'k')
        plt.imshow(wordcloud, interpolation = 'bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)

        wcpath=file+filename

        print(wcpath)

        wordcloud.to_file(wcpath)
        #plt.show()

        # # create a word frequency dictionary
        # wordfreq = Counter(df.tweet_text.to_string( index=False, header=False))
        #
        # wordcloud = WordCloud(
        #     width = 3000,
        #     height = 2000,
        #     background_color = 'black',
        #     #stopwords = STOPWORDS
        # ).generate_from_frequencies(text)
        # #generate(' '.join(str(df['tweet_text']))
        # fig = plt.figure(
        #     figsize = (40, 30),
        #     facecolor = 'k',
        #     edgecolor = 'k')
        # plt.imshow(wordcloud, interpolation = 'bilinear')
        # plt.axis('off')
        # plt.tight_layout(pad=0)
        #
        # wcpath=file+"/tweets_freq.png"
        #
        # print(wcpath)
        #
        # wordcloud.to_file(wcpath)



# class sentimentanalysis():
#
#
#     def sentiment_analysis(self, df):
#
#         textcleaned = df['tweet_text']
#
#         #print(textcleaned)
#
#         #textcleaned = df.tweet_text.to_string(index=False, header=False)
#
#
#
#
#         analysis = TextBlob(textcleaned)
#
#
#         if analysis.sentiment.polarity > 0:
#             return 1
#         elif analysis.sentiment.polarity == 0:
#
#             return 0
#         else:
#             return -1

class sentimentanalysis():


    def analyse_sentiment(self, df):


        sentiment = df

        if sentiment > 0:
            return 1
        elif sentiment == 0:
            return 0
        else:
            return -1


if __name__ == '__main__':


    selectdb = extractDB()
    datapreparation = data_preparation()
    genwordcloud = wordcloud()
    senti=sentimentanalysis()


    df = selectdb.sqlconnect()
    datapreparation.preprocessing(df)
    datapreparation.remove_stopwords(df)
    #datapreparation.analyze_sentiment(df)


    #df['sentiment'] = np.array([datapreparation.analyze_sentiment(df) for df in df['tweet_text']])
    #df['sentiment'] = df['tweet_text'].apply(lambda tweet: senti.sentiment_analysis(df).sentiment)

    #df['sentiment'] = df.tweet_text.apply(lambda tweet_text: TextBlob(tweet_text).sentiment.polarity)

    #print(df)

    df['sentiment'] = df.tweet_text.apply(lambda tweet_text: TextBlob(tweet_text).sentiment.polarity)

    df['sentiment'] = np.array([senti.analyse_sentiment(df) for df in df['sentiment']])

    #print(df)


    #df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])


    #df['sentiment'] = df.tweet_text.apply(lambda tweet_text: TextBlob(tweet_text))
    #appended_data['sentiment'] = appended_data.body.apply(lambda body: TextBlob(body).sentiment)

    #print(df.tweet_text.head(30),df.sentiment.head(30))
    print(df['tweet_text'].iloc[50])
    print(df['tweet_text'].iloc[60])


    #genwordcloud.wordclouddraw(pd.Series([g for g in df[df.sentiment == 1].tweet_text]).str.cat(sep=' '))

    #word_cloud(pd.Series([t for t in tweet_table[tweet_table.sentiment == "Positive"].tweet]).str.cat(sep=' '))

    genwordcloud.wordclouddraw(df, sent="all")
    genwordcloud.wordclouddraw(df, sent="positive")
    genwordcloud.wordclouddraw(df, sent="negative")



#word_cloud(pd.Series([t for t in tweet_table.tweet]).str.cat(sep=' '))
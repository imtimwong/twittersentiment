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

        #put all preprocessing into one class later
        s="SELECT * FROM TWEETS;"


        df = pd.read_sql(s,con, index_col="tweet_id")


        return df


        #print(df['tweet_text'])


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


        print(df['tweet_text'].iloc[50])
        print(df['tweet_text'].iloc[60])


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




class wordcloud():

    def wordclouddraw(self,df,sent):


        #text = df.tweet_text
        #print(textdf)

        if sent == 'positive':

            #https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
            text_filtered_sentiment = df['sentiment'] == 1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/pos_tweets.png"

        elif sent == 'negative':

            text_filtered_sentiment = df['sentiment'] == -1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/neg_tweets.png"

        else:

            text = df.tweet_text.to_string( index=False, header=False)
            filename = "/all_tweets.png"


        #text = text_filtered_sentiment.tweet_text.to_string( index=False, header=False)
        # this one above coorect


        file = os.getcwd()

        print(file)

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

    #https: // stackoverflow.com / questions / 54588807 / loop - to - retrieve - sentiment - analysis - in -pandas - core - series - series
    #add sentiment score into a new column in dataframe
    df['sentiment'] = df.tweet_text.apply(lambda tweet_text: TextBlob(tweet_text).sentiment.polarity)

    #convert sentiment score into 1(positive),-1(negative) or 0(neutral)
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
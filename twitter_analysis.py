#! /usr/local/bin/python3.7

#import for db connection
#import psycopg2
import postgrescredentials

#import for ORM
import sqlalchemy as db

#import for dataframes
import numpy as np
import pandas as pd

#import re

#import nltk
#need to manuall download 'punkt' before using this : nltk.download('punkt')
from nltk.corpus import (stopwords)


#from nltk.tokenize import word_tokenize

#for os commands
import os

#for wordcloud
from wordcloud import WordCloud #, STOPWORDS
import matplotlib.pyplot as plt

#import for Natural language Processing(NLP) sentiment analysis library
from textblob import TextBlob


#import sklearn
from sklearn.feature_extraction.text import (
    CountVectorizer)

import collections
import seaborn as sns
sns.set(style="darkgrid")
sns.set(font_scale=1.3)


class extractDB():
    """
    To read from db
    """

    def sqlconnect(self):

        sqlengine = db.create_engine('postgres+psycopg2://%s:%s@%s:%s/%s'%(postgrescredentials.user,postgrescredentials.password,postgrescredentials.host,postgrescredentials.port,postgrescredentials.database))

        con = sqlengine.connect()

        #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html

        s="SELECT * FROM TWEETS_HAZE;"


        df = pd.read_sql(s,con, index_col="tweet_id")

        return df
        #print(df['tweet_text'])


class data_preparation():
    """
    To clean tweets and remove words that we don't need for analysis
    """

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
        # Removing tweet topic
        df['tweet_text'] = df['tweet_text'].str.replace('haze', '')


        #print(df['tweet_text'].iloc[50])
        #print(df['tweet_text'].iloc[60])


        return df


    def remove_stopwords(self,df):
        """
        Stopwords like the,a,in,an will bring no value to our analysis and it should be removed.
        """

        #https://stackoverflow.com/questions/29523254/python-remove-stop-words-from-pandas-dataframe

        #removing stop words such as "the,a,in,an"
        stop_words_eng = stopwords.words('english')
        #df['tweet_text'] = df['tweet_text'].str.lower()

        #lamda a type of hidden function or anonymous function written in one line instead of writing a new function
        #apply is used to apply the lamda function on one column
        #split the tweet using space in x.split() then check for if its not a stop word then join it together again with space
        #and move on to the next word of the tweet


        df['tweet_text'] = df['tweet_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words_eng)]))
        #print(df['tweet_text'].iloc[50])
        #print(df['tweet_text'].iloc[60])


        return df


        #https://towardsdatascience.com/the-real-world-as-seen-on-twitter-sentiment-analysis-part-one-5ac2d06b63fb
        #tweet = word_tokenize(str(df['tweet_text'].iloc[50])) this works too

        #print(tweet)

        #df['tweet_text'] = df['tweet_text'].apply(word_tokenize) this works




class wordcloud():
    """
    to generate wordcloud based on sentiment value positive, negative and both positive and negative.
    """

    def wordclouddraw(self,df,sent):


        if sent == 'positive':

            #https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
            text_filtered_sentiment = df['sentiment'] == 1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/HAZE_pos_tweets.png"

        elif sent == 'negative':

            text_filtered_sentiment = df['sentiment'] == -1
            text_filtered_sentiment2 = df[text_filtered_sentiment]
            text = text_filtered_sentiment2.tweet_text.to_string(index=False, header=False)
            filename = "/HAZE_neg_tweets.png"

        else:
            #this includes both positive and negative tweets
            text = df.tweet_text.to_string( index=False, header=False)
            filename = "/HAZE_all_tweets.png"



        file = os.getcwd()

        #print(file)

        wordcloud = WordCloud(
            width = 3000,
            height = 2000,
            background_color = 'black',
            #stopwords = STOPWORDS
            stopwords=['haze']
        ).generate(text)
        #generate(' '.join(str(df['tweet_text']))
        fig = plt.figure(
            figsize = (40, 30),
            facecolor = 'k',
            edgecolor = 'k')
        plt.imshow(wordcloud, interpolation = 'bilinear')#'hermite'
        plt.axis('off')
        plt.tight_layout(pad=0)

        wcpath=file+filename

        print(wcpath)

        wordcloud.to_file(wcpath)
        #plt.show()





class sentimentanalysis():
    """
    to convert sentiment score generated from TextBlob library into 1,-1 or 0 based on sentiment score.
    """

    def analyse_sentiment(self, df):


        sentiment = df

        if sentiment > 0:
            return 1
        elif sentiment == 0:
            return 0
        else:
            return -1



class wordfreq():

    """
    to generate a graph based on word frequency
    """

    def vectorization(self, df, sent2):
        # https://towardsdatascience.com/sentiment-analysis-with-text-mining-13dd2b33de27

        countv = CountVectorizer()
        bow = countv.fit_transform(df.tweet_text)
        word_freq = dict(zip(countv.get_feature_names(), np.asarray(bow.sum(axis=0)).ravel()))
        word_counter = collections.Counter(word_freq)
        word_counter_df = pd.DataFrame(word_counter.most_common(30), columns=['word', 'freq'])

        print("in vectorization")
#https://www.drawingfromdata.com/how-to-rotate-axis-labels-in-seaborn-and-matplotlib

        file = os.getcwd()
        title = "Word Frequency for %s tweets" % sent2
        fig, ax = plt.subplots(figsize=(10, 12))
        sns.barplot(x="freq", y="word", data=word_counter_df, palette="PuBuGn_d", ax=ax)

        plt.xticks(
            rotation=90,
            horizontalalignment='right',
            fontweight='light',
            #fontsize='x-large'
            size = 14
        )

        plt.xlabel("Frequency", size=14);
        plt.ylabel("30 more frequent words", size=14);

        plt.title(title, size=18)
        plt.grid(False);
        plt.gca().spines["top"].set_visible(False);
        plt.gca().spines["right"].set_visible(False);




        filename = "/HAZE_graph_%s.png" %sent2
        graphpath = file + filename
        plt.savefig(graphpath, format="png")
        #plt.show()




#https://towardsdatascience.com/natural-language-processing-count-vectorization-with-scikit-learn-e7804269bb5e

if __name__ == '__main__':


    selectdb = extractDB()
    datapreparation = data_preparation()
    genwordcloud = wordcloud()
    senti=sentimentanalysis()
    wf = wordfreq()


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
    #print(df['tweet_text'].iloc[50])
    #print(df['tweet_text'].iloc[60])


    genwordcloud.wordclouddraw(df, sent="all")
    genwordcloud.wordclouddraw(df, sent="positive")
    genwordcloud.wordclouddraw(df, sent="negative")

    #wf.vectorization(df)

    # Graph with frequency words all, positive and negative tweets and get the frequency
    wf.vectorization(df, sent2="all")
    #print (df[df['sentiment'] == 1])
    wf.vectorization(df[df['sentiment'] == 1], sent2="positive")
    wf.vectorization(df[df['sentiment'] == -1], sent2="negative")





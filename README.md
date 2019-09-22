

<!DOCTYPE html>
<html>
# twittersentiment
<body>
<h1>Personal project to analyse tweets for sentiment analysis</h1>


<h2>Why this project?</h2>
<p>The objective is to learn to work with semi-structured data and Python. To stream live tweets and pump it into Postgresql for sentiment analysis.<br>
In the wake off
For this project we will be analysing sentiments on the yearly air pollution .

<h3>Requirements:</ h3>
<p>Tech used: Python, Postgresql, Docker Container, Pycharm</p>
<p>libraries: <a href="http://docs.tweepy.org/en/latest/">tweepy</a>, <a href="http://initd.org/psycopg/docs/install.html">psycopg2</a>, pandas, <a href="https://docs.sqlalchemy.org/en/13/core/tutorial.html">sqlalchemy</a><a href="https://www.nltk.org/install.html">, nltk</a>, numpy</p>

Please refer to <a href="https://github.com/imtimwong/twittersentiment/blob/feature1/streamtweets.py">streamtweets.py</a>, <a href="https://github.com/imtimwong/twittersentiment/blob/master/removeDupDb.py">removeDupDb.py</a>, <a href="https://github.com/imtimwong/twittersentiment/blob/master/twitter_analysis.py">twitter_analysis.py</a>

<h3>Milestones:</h3> 
<ol>
<li>Apply for twitter developer account and credentials. << Done &#10004;</li>
<li>Build basic twitter streamer with authentication and print tweets to screen using <a href="http://docs.tweepy.org/en/latest/">tweepy</a> << Done &#10004;</li>
<li>Seperate features into different classes to enhance reusability << Done &#10004;</li>
<li>Extract tweets from twitter's API JSON format << Done &#10004;</li>
<li>Write tweets into text file (just another option to store data instead of db) << Done &#10004;</li>
<li>Setup Docker for Postgresql(way better than a VM imho) << Done &#10004;</li>
<li>Design and create db tables to store tweets.(maybe create tables on the fly based on analysis topic for future enhancement) << Done &#10004;</li>
<li>Establish database connection to Postgresql with <a href="http://initd.org/psycopg/docs/install.html">psycopg2</a> and test insert into table<< Done &#10004;</li>
<li>Test load tweets into table << Done &#10004;</li>
<li> Running program and streaming and collecting tweets into db << Done &#10004;</li>
<li> Data preparation (cleaning each tweet and removing stopwords with nltk) << Done &#10004;</li>

<li> Getting sentiment score of each tweet with <a href="https://textblob.readthedocs.io/en/dev/"> TextBlob</a> << Done &#10004;</li>

<li> Generating wordclouds based on sentiment score << Done &#10004;</li>
<li> Generating word count frequency graph << WIP &#128736;</li>
<li> More to come...</li>
</ol>

<h4>Analysis results:</h4>
<p>
	<h5>Positive tweets wordcloud:</h5>
	<!--![Image of positive tweets wordcloud]
	(https://raw.github.com/imtimwong/twittersentiment/master/haze_results/final%20run%20haze/HAZE_pos_tweets.png)-->
	<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/haze_results/final%20run%20haze/HAZE_pos_tweets.png" width="550">
	<p>Explanation coming soon...</p>
	<br>
	<h5>Negative tweets wordcloud:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/master/haze_results/final%20run%20haze/HAZE_neg_tweets.png" width="550">
	<br>
	<h5>Positive tweets graph:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/master/haze_results/final%20run%20haze/HAZE_graph_positive.png" width="550">
	<br>
	<h5>Negative tweets graph:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/master/haze_results/final%20run%20haze/HAZE_graph_negative.png" width="550">
	<br>
	

</p>


Current project status: data analysis <br>
Next milestone: data analysis

Ps: Stay tuned for more updates! 


Cheers,<br>
Tim

Have a lovely day! </p>

</body>
</html>




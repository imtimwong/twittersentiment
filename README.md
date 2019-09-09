# twittersentiment
<h1>Personal project to analyse tweets for sentiment analysis</h1>

<h2>Why this project?</h2>
<p>The objective is to learn to work with semi-structured data and Python. To stream live tweets and pump it into Postgresql for sentiment analysis. 

<h3>Requirements:</h3>
<p>Tech used: Python, Postgresql, Docker Container, Pycharm</p>
<p>libraries: <a href="http://docs.tweepy.org/en/latest/">tweepy</a>, <a href="http://initd.org/psycopg/docs/install.html">psycopg2</a>, pandas, <a href="https://docs.sqlalchemy.org/en/13/core/tutorial.html">sqlalchemy</a></p>

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
<li> Data preparation << WIP &#128736;</li>
<li> More to come...</li>
</ol>

Current project status: data preparation and cleansing <br>
Next milestone: data analysis

Ps: Stay tuned for more updates! 


Cheers,<br>
Tim

Have a lovely day! </p>



# twittersentiment

<h1>Personal project to analyse tweets for sentiment analysis</h1>


<h2>Why this project?</h2>
<p>The objective is to pick up new languages, learn to work with semi-structured data and Data Science technologies/stack. To stream live tweets with twitter API for sentiment analysis.<br>

This project is an analysis of the sentiments on the yearly <a href="https://www.businessinsider.my/11-photos-of-the-haze-that-show-why-malaysias-pm-mahathir-is-writing-to-jokowi/">air pollution</a> affecting mainly Malaysia, Singapore and Indonesia. Malaysia has been hit by worsening haze with some areas entering the "unhealthy" zone based on the API(Air pollution index) rating.
<br>

Based on the results of the analysis, we can obtain the public's opinion about the haze and how it's affecting them.

<h3>Project phases :</h3>

This project has two phases. Phase 1 will be using twitter's API and stream tweets using tweepy to store it in Postgresql database for analysis using Python.

Phase 2 will be modifiying and replicating the data preparation, analysis and storage stages in phase 1 using pySpark and Hadoop HDFS instead.

<h3>Requirements:</h3>
<p>Tech used: Python, Postgresql, Docker Container, SQLWorkbenchJ, Pycharm, Jupyter Notebook, Spark, Hadoop</p>
<p>libraries: <a href="http://docs.tweepy.org/en/latest/">tweepy</a>, <a href="http://initd.org/psycopg/docs/install.html">psycopg2</a>, pandas, <a href="https://docs.sqlalchemy.org/en/13/core/tutorial.html">sqlalchemy</a><a href="https://www.nltk.org/install.html">, nltk</a>, TextBlob, numpy, matplotlib, seaborn, wordcloud, sklearn, pyArrow, pySpark</p>

<h3>Program design:</h3>
<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/misc/architecture_diagram.png" alt="Program design architecture diagram" class="center">

<h3>Please refer to :</h3>
<ul>
	<h3>Phase 1 (python,postgresql) :</h3>
	<li><a href="https://github.com/imtimwong/twittersentiment/blob/master/python_streaming_files/streamtweets.py">streamtweets.py</a>: script to live stream tweets from twitter api and load it into postgresql</li>
	<li><a href="https://github.com/imtimwong/twittersentiment/blob/master/python_streaming_files/removeDupDb.py">removeDupDb.py</a>
 	: script to remove duplicated tweets eg: retweets</li>
	<li><a href="https://github.com/imtimwong/twittersentiment/blob/master/python_streaming_files/twitter_analysis.py">twitter_analysis.py</a> : script for data preparation and analysis using Postgresql</li>
	<h3>Phase 2 (pySpark, Hadoop) :</h3>
	<li><a href="https://github.com/imtimwong/twittersentiment/blob/master/python_streaming_files/export_to_text_file.py">export_to_text_file.py</a> : script to export tweets from postgresql to text file</li>
	<li><a href="https://nbviewer.jupyter.org/github/imtimwong/twittersentiment/blob/master/jupyter_notebook_analysis_files/twitter_analysis_spark_hadoop.ipynb">twitter_analysis_spark_hadoop.ipynb</a> or <a href="https://github.com/imtimwong/twittersentiment/blob/master/jupyter_notebook_analysis_files/twitter_analysis_spark_hadoop.pdf">twitter_analysis_spark_hadoop.pdf</a> : script for data preparation and analysis for spark and hadoop(<b>*without explanation</b>) 
	<li><a href="https://nbviewer.jupyter.org/github/imtimwong/twittersentiment/blob/master/jupyter_notebook_analysis_files/twitter_analysis_spark_hadoop_breakdown.ipynb">twitter_analysis_spark_hadoop_breakdown.ipynb</a> or <a href="https://github.com/imtimwong/twittersentiment/blob/master/jupyter_notebook_analysis_files/twitter_analysis_spark_hadoop_breakdown.pdf">twitter_analysis_spark_hadoop_breakdown.pdf</a> : script for data preparation and analysis for spark and hadoop (<b>**with breakdown explanation</b>) for each function and result (pls click this link instead of the one uploaded in this repo due to issues to load on github. Pls choose the pdf version if ipynb doesn't work)</li>
</ul>


<h3>Milestones:</h3> 

<h4>Phase 1 :</h4> 
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
<li> Generating word count frequency graph << Done &#10004;</li>
<li> Experimenting on pyspark and hadoop. Possible plans to add in spark and hadoop << Done &#10004;</li></li>


</ol>

<h4>Phase 2 (adding pySpark and Hadoop to replicate analysis part in Phase 1):</h4> 
<ol>
<li>Setup docker containers for Jupyter with pySpark and Hadoop HDFS << Done &#10004;</li>
<li>Export tweets from postgresql into text file and load it into HDFS << Done &#10004;</li>
<li>Load tweets from text file stored in HDFS into Spark dataframes and convert into Pandas dataframes using pyArrow << Done &#10004;</li>
<li>Data preparation/cleaning << data preparation test successful << Done &#10004;
You'll be able to see the transformation of the tweets in <a href="https://github.com/imtimwong/twittersentiment/blob/master/jupyter_notebook_analysis_files/twitter_analysis_spark_hadoop_breakdown.pdf">twitter_analysis_spark_hadoop_breakdown.ipynb</a> (pls click this link instead of the one uploaded in this repo due to issues to load on github. pls click reload if it doesn't load)</li>
<li>Adding explantion and data samples in twitter_analysis_spark_hadoop_breakdown.ipynb << Done &#10004;</li>
<li>Produce program design architecture flow diagram.<< Done &#10004;</li>
<li> More to come...</li>

<br>
Current project status: data analysis <br>
Next milestone: data analysis
<br>
<br>
Ps: Stay tuned for more updates! 


Cheers,<br>
Tim

How do you climb a mountain? <br>

One step at a time.<br>

Make progress or make excuses

Have a lovely day! </p>


<h4>Analysis results (Phase 2):</h4>
<p>
	<h5>Positive tweets wordcloud:</h5>
	<!--![Image of positive tweets wordcloud]
	(https://raw.github.com/imtimwong/twittersentiment/master/haze_results/final%20run%20haze/HAZE_pos_tweets.png) << WIP &#128736;</li> test-->
	<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/haze_results/final%20run%20haze/results%20Phase%202%20using%20pySpark%20Hadoop/HAZE_pos_tweets_spark.png" width="550" alt="Positive tweets wordcloud">
	<br>
	<h5>Negative tweets wordcloud:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/haze_results/final%20run%20haze/results%20Phase%202%20using%20pySpark%20Hadoop/HAZE_neg_tweets_spark.png" width="550" alt="Negative tweets wordcloud">
	<br>
	<h5>Positive tweets graph:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/haze_results/final%20run%20haze/results%20Phase%202%20using%20pySpark%20Hadoop/HAZE_graph_positive_spark.png" width="550" alt="Positive tweets graph">
	<br>
	<h5>Negative tweets graph:</h5>
	<img src="https://github.com/imtimwong/twittersentiment/blob/feature1/haze_results/final%20run%20haze/results%20Phase%202%20using%20pySpark%20Hadoop/HAZE_graph_negative_spark.png" width="550" alt="Negative tweets graph">
	<br>
	<h4>Summary</h4>
	<p>We can see that people are mostly expressing thier frustration about the haze and we can know which countries are affected by it.<br>
		<br>
	For now, I'm still looking for solutions to handle situations like "not bad" or "not good". "not bad" isn't a negative term and "not good" isn't a positive term, using certain NLP libraries might detect a false positive. Plus, adding features to detect sarcasm will help in increasing accuracy for text analysis. Future phases will have additional features such as stemming, lexicon normalization and lemmetization.
	</p>
	<p>
	Analysing tweets can have many use cases, especially in consumer businesses like brand monitoring, product launches insights, customer support email analysis, voice of customer(VOC) or feedback analysis.</p>
	

</p>







# twittersentiment
<h1>Personal project to analyse tweets for sentiment analysis</h1>

<h2>Why this project?</h2>
<p>The objective is to learn to work with semi-structured data and Python. To stream live tweets and pump it into Postgresql for sentiment analysis. (Tech used: Python, Postgresql, Docker Container, tweepy, psycopg2, Pycharm)

Please refer to <a href="https://github.com/imtimwong/twittersentiment/blob/feature1/teststream.py">teststream.py</a>.

Milestones: 
1. Apply for twitter developer account and credentials. << Done &#10004;
2. Build basic twitter streamer with authentication and print tweets to screen using Tweepy << Done &#10004;
3. Seperate features into different classes to enhance reusability << Done &#10004;
4. Extract tweets from twitter's API JSON format << Done &#10004;
5. Write tweets into text delimited text file (just another option to store data instead of db) << Done &#10004;
6. Setup Docker for Postgresql(way better than a vm imho) << Done &#10004;
7. Design and create db tables to store tweets.(maybe create tables on the fly based on analysis topic for future enhancement) << Done &#10004;
8. Establish database connection to Postgresql with psycopg2 and test insert into table<< Done &#10004;
9. Test load tweets into table << WIP &#128736;
10. More to come...


Current project status: Test load tweets into table. <br>
Next milestone: add db feature into main program.

Ps: Stay tuned for more updates! 


Cheers,<br>
Tim

Have a lovely day! </p>



import psycopg2
import postgrescredentials

connection = psycopg2.connect(user=postgrescredentials.user,
                              password=postgrescredentials.password,
                              host=postgrescredentials.host,
                              port=postgrescredentials.port,
                              database=postgrescredentials.database)
cursor = connection.cursor()
cursor2 = connection.cursor()



path='/Users/tim/PycharmProjects/twittersentiment/tweets_pg_export.txt'

sql = "COPY (SELECT TWEET_TEXT FROM TWEETS_HAZE) TO STDOUT WITH CSV DELIMITER ';'"
with open(path, "w") as file:
    cursor.copy_expert(sql, file)

cursor.close()
connection.close()
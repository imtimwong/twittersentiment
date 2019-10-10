

import psycopg2
import postgrescredentials

connection = psycopg2.connect(user=postgrescredentials.user,
                              password=postgrescredentials.password,
                              host=postgrescredentials.host,
                              port=postgrescredentials.port,
                              database=postgrescredentials.database)
cursor = connection.cursor()
cursor2 = connection.cursor()

'''This script is to export data from postgreslql to text file'''


path='/Users/tim/PycharmProjects/twittersentiment/tweets_pg_export2.txt'

sql = "COPY (SELECT TWEET_TEXT FROM TWEETS_HAZE) TO STDOUT WITH CSV HEADER DELIMITER ';'"
with open(path, "w") as file:
    cursor.copy_expert(sql, file)

cursor.close()
connection.close()
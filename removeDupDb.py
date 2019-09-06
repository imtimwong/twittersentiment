#! /usr/local/bin/python3.7

import psycopg2
import postgrescredentials


#reads from postgresl credentials file to connect to db
connection_rem = psycopg2.connect(user=postgrescredentials.user,
                              password=postgrescredentials.password,
                              host=postgrescredentials.host,
                              port=postgrescredentials.port,
                              database=postgrescredentials.database)

cursor_removeDup = connection_rem.cursor()

removeDupSQL="DELETE FROM TWEETS WHERE tweet_id IN (SELECT tweet_id FROM (SELECT tweet_id, ROW_NUMBER() OVER( PARTITION BY tweet_text ORDER BY  tweet_id ) AS row_num FROM TWEETS ) t WHERE t.row_num > 1 );"


cursor_removeDup.execute(removeDupSQL)

print(removeDupSQL)

connection_rem.commit()

print("Records removed from table")

cursor_removeDup.close()
connection_rem.close()




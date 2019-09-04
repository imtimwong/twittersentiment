#! /usr/local/bin/python3.7

import psycopg2
import postgrescredentials

try:
    connection = psycopg2.connect(user = postgrescredentials.user,
                                  password = postgrescredentials.password,
                                  host = postgrescredentials.host,
                                  port = postgrescredentials.port,
                                  database = postgrescredentials.database)
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
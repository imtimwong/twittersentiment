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
    #print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    ##print("You are connected to - ", record,"\n")

    insert_sql = "INSERT INTO testme3 (something) VALUES (%s);"
    insert_values = ('test insert into table')

    cursor.execute(insert_sql, (insert_values,))


    connection.commit()

    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")


except (Exception, psycopg2.Error) as error :
    print ("Failed to insert into table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
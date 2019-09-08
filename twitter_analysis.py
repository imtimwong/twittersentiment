#! /usr/local/bin/python3.7

#import for db connection
import psycopg2
import postgrescredentials

#import for ORM
import sqlalchemy as db

#import
import numpy as np
import pandas as pd



sqlengine = db.create_engine('postgres+psycopg2://%s:%s@%s:%s/%s'%(postgrescredentials.user,postgrescredentials.password,postgrescredentials.host,postgrescredentials.port,postgrescredentials.database))






#if __name__ == '__main__':
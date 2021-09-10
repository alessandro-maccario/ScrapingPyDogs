import pandas as pd
import pymysql.cursors
import mysql.connector
from mysql.connector import errorcode

# TODO
## USE THIS FILE TO INSERT:
## - REFERENCES BETWEEN TABLES
## - COLUMNS IN TABLES LIKE "ID_BREED_GROUP" AND "ADAPTABILITY_ID" WITH REFERENCES.



import pandas as pd
import pymysql
from sqlalchemy import create_engine

user = 'root'
passw = 'tiger'
host =  'localhost'  # either localhost or ip e.g. '172.17.0.2' or hostname address
port = 3306
database = 'breeds_group'

engine = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

# directory = r'directoryLocation'  # path of csv file
# csvFileName = 'something.csv'
#
# df = pd.read_csv(os.path.join(directory, csvFileName ))

dogs_breed_group.to_sql(name='dog_breed_group', con=engine, if_exists = 'append', index=False)

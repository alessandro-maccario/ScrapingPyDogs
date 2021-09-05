import mysql.connector

# CONNECT TO MYSQL
cnx = mysql.connector.connect(user='root',
                              password='tiger',
                              host='localhost')

# CREATE A CURSOR TO INTERACT WITH MYSQL SERVER USING MYSQLCONNECTION OBJECT
cursor = cnx.cursor()

# DROP DB IF EXISTS
drop_db = "DROP DATABASE IF EXISTS `dogs_scraping`"
cursor.execute(drop_db)

# CREATE DB IF NOT EXISTS
creating_db = "CREATE DATABASE `dogs_scraping` DEFAULT CHARACTER SET utf8"
cursor.execute(creating_db)

# ACTIVATE THE SPECIFIC DB
use_db = 'USE dogs_scraping'
cursor.execute(use_db)


################################################
# TODO
## CREATE ONE TABLE & TRY TO INSERT IN THAT DATABASE
## USE THE FOLLOWING CODE BUT CONVERT STRING INSIDE
## WITH THE CODE FROM REVERSE ENGINEERING ABOUT MYSQL

sql = '''CREATE TABLE foo (
       bar VARCHAR(50) DEFAULT NULL
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1
       '''
cursor.execute(sql)
################################################
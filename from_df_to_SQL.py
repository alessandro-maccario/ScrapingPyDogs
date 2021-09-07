import csv
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

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
# CREATE TABLES
# TABLES = dict()
# TABLES['breeds'] = (
#     ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds` (
#      `id` INT(10) UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
#      `id_breed_group` INT(10) UNSIGNED NOT NULL,
#      `name` VARCHAR(100) NOT NULL,
#      `description` TEXT NOT NULL,
#      `url_image` VARCHAR(256) NOT NULL,
#      `adaptability_id` INT(10) UNSIGNED NOT NULL,
#      `height` VARCHAR(100) NULL DEFAULT NULL,
#      `weight` VARCHAR(100) NULL DEFAULT NULL,
#      `life_span` VARCHAR(100) NULL DEFAULT NULL,
#      PRIMARY KEY (`id`),
#      UNIQUE INDEX `name` (`name` ASC),
#      INDEX `fk_breed_in_group_idx` (`id_breed_group` ASC),
#      INDEX `fk_breeds_adaptability1_idx` (`adaptability_id` ASC),
#      CONSTRAINT `fk_breed_in_group` FOREIGN KEY (`id_breed_group`)
#        REFERENCES `dogs`.`breeds_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#      CONSTRAINT `fk_breeds_adaptability1` FOREIGN KEY (`adaptability_id`)
#        REFERENCES `dogs`.`adaptability` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
#     ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')
#
# TABLES['breeds_group'] = (
#     ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds_group` (
#         `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
#         `name` VARCHAR(100) NOT NULL,
#         PRIMARY KEY (`id`),
#         UNIQUE INDEX `name` (`name` ASC)) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')
#
# TABLES['adaptability'] = (
#    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`adaptability` (
#     `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
#     `apartment_living` INT(11) NOT NULL,
#     `good_for_novice_owner` TEXT NOT NULL,
#     `sensitivity` INT(11) NOT NULL,
#     `tolerates_being_alone` INT(11) NOT NULL,
#     `tolerates_cold_weather` INT(11) NOT NULL,
#     `tolerates_hot_weather` INT(11) NOT NULL,
#     PRIMARY KEY (`id`)) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')


##################################################
# CREATE TABLE
TABLES = {}
TABLES['breeds'] = (
    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds` (
     `id` INT(10) UNIQUE NOT NULL AUTO_INCREMENT,
     `name` VARCHAR(100) UNIQUE NOT NULL,
     `description` TEXT NOT NULL,
     PRIMARY KEY (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')

##################################################

# FOR EACH TABLE IN TABLES CREATE TABLE AND HANDLING EXCEPTION
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("WAITING PLEASE...")
        cursor.execute(table_description)
        print(f"Creating table {table_name}: ", end='')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
        print("--- --- --- --- --- --- --- --- --- ---")

################################################

# TODO
## MISSING: INSERTING DATA INSIDE TABLES FROM CSV!

# TODO
## TRY INSERT FIRST ONLY THE FIRST LINE OF BREEDS TABLE WITH THE FOLLOWING DATA:
## ID = 1; ID_BREED_GROUP = 1; NAME = DOGS_NAME; DESCRIPTION = DOGS_DESCRIPTION; URL_IMAGE = DOGS_URL_IMAGE;
## ADAPTABILITY_ID = REFERENCE THE ADAPTABILITY TABLE (TO UNDERSTAND BETTER); HEIGHT = DOGS_HEIGHT; WEIGHT = DOGS_WIGHT;
## LIFE_SPAN = DOGS_LIFE_SPAN;
## FOR  ID_BREED_GROUP YOU HAVE:
## - KNOW HOW MANY CLASS THERE ARE IN THE ATTRIBUTE
## - FOR EACH CLASS GIVE IT A NUMBER
## - THEN YOU HAVE YOUR ID_BREED_GROUP = SOME_NUMBER
## YOU CAN TRY WITH SOMETHING LIKE THIS:

################################################
# READ THE DATAFRAME
csv_data = pd.read_csv('out.csv', header=0, encoding = 'utf8', delimiter=",", sep=' *, *', skipinitialspace = True)

# TAKE ONLY THE FIRST COLUMN (NAME)
dogs_name = csv_data.iloc[:,0]

# TAKE ONLY THE SECOND COLUMN (DESCRIPTION)
dogs_description = csv_data.iloc[:,1]

# CONCATENATE SERIES AND CONVERT TO DATAFRAME
dogs_df = pd.concat([dogs_name, dogs_description], axis=1)

# QUERIES
to_SQL = """INSERT INTO `dogs_scraping`.`breeds` (name, description) VALUES (%s, %s)"""

# CYCLE THROUGH DATAFRAME AND SAVE ROWS TO MYSQL
for index, row in dogs_df.iterrows():
    try:
        cursor.execute(to_SQL, ( row['name'], row['description'], ))
        cnx.commit()
    except:
        print("MISSING SOMETHING!")

print("INSERTING OPERATION: DONE")

cursor.close()
################################################

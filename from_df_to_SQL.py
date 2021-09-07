import csv
import numpy as np
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

cursor.execute("SET FOREIGN_KEY_CHECKS=0")

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
#        REFERENCES `dogs_scraping`.`breeds_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
#      CONSTRAINT `fk_breeds_adaptability1` FOREIGN KEY (`adaptability_id`)
#        REFERENCES `dogs_scraping`.`adaptability` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
     `id` INT(10) UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
     `name` VARCHAR(100) NOT NULL,
     `description` TEXT NOT NULL,
     `url_image` VARCHAR(256) NOT NULL,
     `height` VARCHAR(100) NULL DEFAULT NULL,
     `weight` VARCHAR(100) NULL DEFAULT NULL,
     `life_span` VARCHAR(100) NULL DEFAULT NULL,
     PRIMARY KEY (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')

TABLES['adaptability'] = (
   ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`adaptability` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `adapts_well_to_apartment_living` INT(11) NOT NULL,
    `good_for_novice_owners` TEXT NOT NULL,
    `sensitivity_level` INT(11) NOT NULL,
    `tolerates_being_alone` INT(11) NOT NULL,
    `tolerates_cold_weather` INT(11) NOT NULL,
    `tolerates_hot_weather` INT(11) NOT NULL,
    `affectionate_with_family` INT(11) NOT NULL,
    `kid_friendly` INT(11) NOT NULL,
    `dog_friendly` INT(11) NOT NULL,
    `friendly_toward_strangers` INT(11) NOT NULL,
    `amount_of_shedding` INT(11) NOT NULL,
    `drooling_potential` INT(11) NOT NULL,
    `easy_to_groom` INT(11) NOT NULL,
    `general_health` INT(11) NOT NULL,
    `potential_for_weight_gain` INT(11) NOT NULL,
    `size` INT(11) NOT NULL,
    `easy_to_train` INT(11) NOT NULL,
    `intelligence` INT(11) NOT NULL,
    `potential_for_mouthiness` INT(11) NOT NULL,
    `prey_drive` INT(11) NOT NULL,
    `tendency_to_bark_or_howl` INT(11) NOT NULL,
    `wanderlust_potential` INT(11) NOT NULL,
    `energy_level` INT(11) NOT NULL,
    `intensity` INT(11) NOT NULL,
    `exercise_needs` INT(11) NOT NULL,
    `potential_for_playfulness` INT(11) NOT NULL,
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
# READ THE DATAFRAME. MAINTAIN NULL VALUES AS EMPTY STRING
csv_data = pd.read_csv('out.csv',
                       header=0,
                       encoding = 'utf8',
                       delimiter=",",
                       sep=' *, *',
                       skipinitialspace = True,
                       na_filter=False)
################################################
# "BREEDS" TABLE
# TAKE SINGLE COLUMNS FOR "BREEDS" TABLE
# TAKE ONLY THE FIRST COLUMN (NAME)
dogs_name = csv_data.iloc[:,0]

# TAKE ONLY THE SECOND COLUMN (DESCRIPTION)
dogs_description = csv_data.iloc[:,1]

# TAKE ONLY THE THIRD COLUMN (URL_IMAGE)
dogs_image = csv_data.iloc[:,2]

# TAKE ONLY THE 30TH COLUMN (HEIGHT)
dogs_height = csv_data.iloc[:,30]

# TAKE ONLY THE 31TH COLUMN (WEIGHT)
dogs_weight = csv_data.iloc[:,31]

# TAKE ONLY THE 32TH COLUMN (LIFE_SPAN)
dogs_lifeSpan = csv_data.iloc[:,32]

# CONCATENATE SERIES AND CONVERT TO DATAFRAME
dogs_df = pd.concat([dogs_name,
                     dogs_description,
                     dogs_image,
                     dogs_height,
                     dogs_weight,
                     dogs_lifeSpan], axis=1)

################################################
# ADAPTABILITY TABLE
# TAKE SINGLE COLUMNS FOR "ADAPTABILITY" TABLE

# TAKE ONLY THE THIRD COLUMN (ADAPTS_WELL_TO_APARTMENT_LIVING)
dogs_apartments = csv_data.iloc[:,3]

# TAKE ONLY THE SECOND COLUMN (GOOD_FOR_NOVICE_OWNERS)
dogs_novice_owners = csv_data.iloc[:,4]

# TAKE ONLY THE 30TH COLUMN (SENSITIVITY_LEVEL)
dogs_sensitivity_level = csv_data.iloc[:,5]

# TAKE ONLY THE 31TH COLUMN (TOLERATES_BEING_ALONE)
dogs_being_alone = csv_data.iloc[:,6]

# TAKE ONLY THE 32TH COLUMN (TOLERATES_COLD_WEATHER)
dogs_cold_weather= csv_data.iloc[:,7]

# TAKE ONLY THE 32TH COLUMN (TOLERATES_HOT_WEATHER)
dogs_hot_weather = csv_data.iloc[:,8]

# TAKE ONLY THE 32TH COLUMN (AFFECTIONATE_WITH_FAMILY)
dogs_affectionate_with_family = csv_data.iloc[:,9]

# TAKE ONLY THE 32TH COLUMN (KID_FRIENDLY)
dogs_kid_friendly = csv_data.iloc[:,10]

# TAKE ONLY THE 32TH COLUMN (DOG_FRIENDLY)
dogs_dog_friendly = csv_data.iloc[:,11]

# TAKE ONLY THE 32TH COLUMN (FRIENDLY_TOWARD_STRANGERS)
dogs_friendly_toward_stranger = csv_data.iloc[:,12]

# TAKE ONLY THE 32TH COLUMN (AMOUNT_OF_SHEDDING)
dogs_amount_of_shedding = csv_data.iloc[:,13]

# TAKE ONLY THE 32TH COLUMN (DROOLING_POTENTIAL)
dogs_drooling_potential = csv_data.iloc[:,14]

# TAKE ONLY THE 32TH COLUMN (EASY_TO_GROOM)
dogs_easy_to_groom = csv_data.iloc[:,15]

# TAKE ONLY THE 32TH COLUMN (GENERAL_HEALTH)
dogs_general_health = csv_data.iloc[:,16]

# TAKE ONLY THE 32TH COLUMN (POTENTIAL_FOR_WEIGHT_GAIN)
dogs_potential_weight_gain = csv_data.iloc[:,17]

# TAKE ONLY THE 32TH COLUMN (SIZE)
dogs_size = csv_data.iloc[:,18]

# TAKE ONLY THE 32TH COLUMN (EASY_TO_TRAIN)
dogs_easy_to_train = csv_data.iloc[:,19]

# TAKE ONLY THE 32TH COLUMN (INTELLIGENCE)
dogs_intelligence = csv_data.iloc[:,20]

# TAKE ONLY THE 32TH COLUMN (POTENTIAL_FOR_MOUTHINESS)
dogs_potential_mouthiness = csv_data.iloc[:,21]

# TAKE ONLY THE 32TH COLUMN (PREY_DRIVE)
dogs_prey_drive = csv_data.iloc[:,22]

# TAKE ONLY THE 32TH COLUMN (TENDENCY_TO_BARK_OR_HOWL)
dogs_tendency_bark_howl = csv_data.iloc[:,23]

# TAKE ONLY THE 32TH COLUMN (WANDERLUST_POTENTIAL)
dogs_wanderlust_potential = csv_data.iloc[:,24]

# TAKE ONLY THE 32TH COLUMN (ENERGY_LEVEL)
dogs_energy_level = csv_data.iloc[:,25]

# TAKE ONLY THE 32TH COLUMN (INTENSITY)
dogs_intensity = csv_data.iloc[:,26]

# TAKE ONLY THE 32TH COLUMN (EXERCISE_NEEDS)
dogs_exercise_needs = csv_data.iloc[:,27]

# TAKE ONLY THE 32TH COLUMN (POTENTIAL_FOR_PLAYFULNESS)
dogs_potential_playfulness = csv_data.iloc[:,28]

# CONCATENATE SERIES AND CONVERT TO DATAFRAME
adaptability_df = pd.concat([
    dogs_apartments,
    dogs_novice_owners,
    dogs_sensitivity_level,
    dogs_being_alone,
    dogs_cold_weather,
    dogs_hot_weather,
    dogs_affectionate_with_family,
    dogs_kid_friendly,
    dogs_dog_friendly,
    dogs_friendly_toward_stranger,
    dogs_amount_of_shedding,
    dogs_drooling_potential,
    dogs_easy_to_groom,
    dogs_general_health,
    dogs_potential_weight_gain,
    dogs_size,
    dogs_easy_to_train,
    dogs_intelligence,
    dogs_potential_mouthiness,
    dogs_prey_drive,
    dogs_tendency_bark_howl,
    dogs_wanderlust_potential,
    dogs_energy_level,
    dogs_intensity,
    dogs_exercise_needs,
    dogs_potential_playfulness], axis=1)

adaptability_df.replace(np.NaN, ' ', inplace=True)
################################################
# QUERIES
to_SQL_breeds = """INSERT INTO `dogs_scraping`.`breeds` (name, description, url_image, height, weight, life_span) VALUES 
(%s, %s, %s, %s, %s, %s)"""

to_SQL_adaptability = """ 
INSERT INTO `dogs_scraping`.`adaptability` (
adapts_well_to_apartment_living, 
good_for_novice_owners, 
sensitivity_level, 
tolerates_being_alone,
tolerates_cold_weather, 
tolerates_hot_weather, 
affectionate_with_family, 
kid_friendly, 
dog_friendly, 
friendly_toward_strangers, 
amount_of_shedding, 
drooling_potential, 
easy_to_groom, 
general_health, 
potential_for_weight_gain, 
size, 
easy_to_train, 
intelligence, 
potential_for_mouthiness, 
prey_drive, 
tendency_to_bark_or_howl, 
wanderlust_potential,
energy_level,
intensity, 
exercise_needs, 
potential_for_playfulness) 
VALUES (%s, %s, %s, %s, %s, %s, 
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

################################################
# CYCLE THROUGH DATAFRAME AND SAVE ROWS TO MYSQL
for index, row in dogs_df.iterrows():
    try:
        cursor.execute(to_SQL_breeds,
                       ( row['name'],
                         row['description'],
                         row['image'],
                         row['height'],
                         row['weight'],
                         row['life_span']))
        cnx.commit()
    except:
        print("MISSING SOMETHING!")
        continue

print("INSERTING OPERATION: FIRST TABLE DONE!")

for index, row in adaptability_df.iterrows():
    try:
        cursor.execute(to_SQL_adaptability,
                       ( row['adapts_well_to_apartment_living'],
                         row['good_for_novice_owners'],
                         row['sensitivity_level'],
                         row['tolerates_being_alone'],
                         row['tolerates_cold_weather'],
                         row['tolerates_hot_weather'],
                         row['affectionate_with_family'],
                         row['kid_friendly'],
                         row['dog_friendly'],
                         row['friendly_toward_strangers'],
                         row['amount_of_shedding'],
                         row['drooling_potential'],
                         row['easy_to_groom'],
                         row['general_health'],
                         row['potential_for_weight_gain'],
                         row['size'],
                         row['easy_to_train'],
                         row['intelligence'],
                         row['potential_for_mouthiness'],
                         row['prey_drive'],
                         row['tendency_to_bark_or_howl'],
                         row['wanderlust_potential'],
                         row['energy_level'],
                         row['intensity'],
                         row['exercise_needs'],
                         row['potential_for_playfulness']))
        cnx.commit()
    except:
        print("MISSING SOMETHING!")
        continue

print("INSERTING OPERATION: SECOND TABLE DONE!")
################################################
cursor.close()

# TODO
## NEED TO CORRECT MISSING VALUES IN THE SECOND TABLE
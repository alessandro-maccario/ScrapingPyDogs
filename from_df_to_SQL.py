import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import errorcode

# CONNECT TO MYSQL
cnx = mysql.connector.connect(user='root',
                              password='tiger',
                              host='localhost',
                              autocommit=True)

# CREATE A CURSOR TO INTERACT WITH MYSQL SERVER USING MYSQLCONNECTION OBJECT
# EXPLANATION OF BUFFERED=TRUE:
# https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
cursor = cnx.cursor(buffered=True)

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

##################################################
# CREATE TABLE
TABLES = dict()
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

TABLES['breeds_group'] = (
    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds_group` (
        `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `dog_breed_group` VARCHAR(200) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `dog_breed_group` (`dog_breed_group` ASC)
        ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARACTER SET = utf8 ''')

TABLES['breeds'] = (
    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds` (
     `id` INT(10) UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
     `name` VARCHAR(100) NOT NULL,
     `description` TEXT NOT NULL,
     `url_image` VARCHAR(256) NOT NULL,
     `adaptability_id` INT(10) UNSIGNED NOT NULL,
     `height` VARCHAR(100) NULL DEFAULT NULL,
     `weight` VARCHAR(100) NULL DEFAULT NULL,
     `life_span` VARCHAR(100) NULL DEFAULT NULL,
     PRIMARY KEY (`id`),
     UNIQUE INDEX `name` (`name` ASC),
     INDEX `fk_breed_in_group_idx` (`id` ASC),
     INDEX `fk_breeds_adaptability1_idx` (`id` ASC),
     CONSTRAINT `fk_breed_in_group` FOREIGN KEY (`id`)
       REFERENCES `dogs_scraping`.`breeds_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
     CONSTRAINT `fk_breeds_adaptability1` FOREIGN KEY (`id`)
       REFERENCES `dogs_scraping`.`adaptability` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
# READ THE DATAFRAME. MAINTAIN NULL VALUES AS EMPTY STRING
csv_data = pd.read_csv('out.csv',
                       encoding='utf8',
                       na_filter=False)
################################################
# "BREEDS" TABLE
# CREATE A DATABASE THAT CONTAINS NAME, DESCRIPTION, URL_IMAGE, HEIGHT, WEIGHT, LIFE_SPAN
# INDEX: 0, 1, 2, 30, 31, 32

dogs_df = pd.DataFrame(csv_data.iloc[:, [0, 1, 2, 30, 31, 32]])
# ADAPTABILITY TABLE
adaptability_df = pd.DataFrame(csv_data.iloc[1:, 3:29])

# ADD THREE VALUE AT HAND THAT, AT FIRST, THE PREVIOUS CODE FAIL TO RECOGNISE EVEN
# THAT THEY WERE THERE IN THE CSV FILE.
# FIRST VALUE = ROW INDEX NUMBER; SECOND VALUE = COLUMN; VALUE AFTER EQUAL SIGN = THE VALUE TO INSERT IN DATASET
adaptability_df.at[163, 'potential_for_playfulness'] = 4
adaptability_df.at[237, 'potential_for_playfulness'] = 5
adaptability_df.at[317, 'potential_for_playfulness'] = 5

# BREED_GROUP TABLE
# TAKE SINGLE COLUMN FOR "BREED_GROUP" TABLE
dogs_breed_group = pd.DataFrame(csv_data.iloc[:, 29])

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
potential_for_playfulness) VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

to_SQL_breeds_groups = """INSERT INTO `dogs_scraping`.`breeds_group` (`dog_breed_group`) VALUES (?,)"""

################################################
# CONNECT TO THE CORRECT DATABASE
engine = create_engine('mysql+pymysql://root:tiger@localhost:3306/dogs_scraping', echo=False)

# INSERT DATA TO THE FIRST TABLE
dogs_df.to_sql(name='breeds', con=engine, if_exists='replace', index=False)
cursor.execute("""ALTER TABLE `breeds` ADD `id` INT PRIMARY KEY AUTO_INCREMENT;""")

print("INSERTING OPERATION: FIRST TABLE DONE!")

# INSERT DATA TO THE SECOND TABLE
adaptability_df.to_sql(name='adaptability', con=engine, if_exists='replace', index=False)
cursor.execute("""ALTER TABLE `adaptability` ADD `id` INT PRIMARY KEY AUTO_INCREMENT;""")

print("INSERTING OPERATION: SECOND TABLE DONE!")

# INSERT DATA TO THE THIRD TABLE
dogs_breed_group.to_sql(name='breeds_group', con=engine, if_exists='replace', index=False)
cursor.execute("""ALTER TABLE `breeds_group` ADD `id` INT PRIMARY KEY AUTO_INCREMENT;""")

print("INSERTING OPERATION: THIRD TABLE DONE!")

################################################
# # TRY TO FETCH FROM MYSQL
# # ACTIVATE THE SPECIFIC DB
# use_db = 'USE dogs_scraping'
# cursor.execute(use_db)
#
# # TRY A SELECT STATEMENT
# cursor.execute("""
# SELECT breeds_group.dog_breed_group, breeds.name
# FROM breeds_group
# LEFT JOIN breeds on breeds_group.id = breeds.id
# WHERE breeds_group.dog_breed_group = 'Mixed Breed Dogs';
# """)
#
# # SAVE THE LAST CALL TO THE DATABASE
# result = cursor.fetchall()
# # PRINT THE RESULT
# print(result)
#
# # WRITE THE LAST QUERY TO A TXT FILE (THE OUTPUT OF RESULT IS A TUPLE)
# with open('file_name.txt', 'w') as f:
#     for row in result:
#         f.write('%s %s\n' % row)
################################################
# CLOSE THE CURSOR
cursor.close()

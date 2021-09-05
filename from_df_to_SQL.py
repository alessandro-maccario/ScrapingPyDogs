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
# CREATE TABLES
TABLES = {}
TABLES['breeds'] = (
    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds` (
     `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
     `id_breed_group` INT(10) UNSIGNED NOT NULL,
     `name` VARCHAR(100) NOT NULL,
     `description` TEXT NOT NULL,
     `url_image` VARCHAR(256) NOT NULL,
     `adaptability_id` INT(10) UNSIGNED NOT NULL,
     `height` VARCHAR(100) NULL DEFAULT NULL,
     `weight` VARCHAR(100) NULL DEFAULT NULL,
     `life_span` VARCHAR(100) NULL DEFAULT NULL,
     PRIMARY KEY (`id`),
     UNIQUE INDEX `name` (`name` ASC),
     INDEX `fk_breed_in_group_idx` (`id_breed_group` ASC),
     INDEX `fk_breeds_adaptability1_idx` (`adaptability_id` ASC),
     CONSTRAINT `fk_breed_in_group` FOREIGN KEY (`id_breed_group`)
       REFERENCES `dogs`.`breeds_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
     CONSTRAINT `fk_breeds_adaptability1` FOREIGN KEY (`adaptability_id`)
       REFERENCES `dogs`.`adaptability` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
    ) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ''')

TABLES['breeds_group'] = (
    ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`breeds_group` (
        `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `name` (`name` ASC)) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ''')

TABLES['adaptability'] = (
   ''' CREATE TABLE IF NOT EXISTS `dogs_scraping`.`adaptability` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `apartment_living` INT(11) NOT NULL,
    `good_for_novice_owner` TEXT NOT NULL,
    `sensitivity` INT(11) NOT NULL,
    `tolerates_being_alone` INT(11) NOT NULL,
    `tolerates_cold_weather` INT(11) NOT NULL,
    `tolerates_hot_weather` INT(11) NOT NULL,
    PRIMARY KEY (`id`)) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ''')

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
## MISSING INSERTING DATA INSIDE TABLES FROM CSV!
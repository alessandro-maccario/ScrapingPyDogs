import mysql.connector
from mysql.connector import errorcode


# TODO
## PROBLEM: INCAPABLE OF CREATING TABLES INSIDE THE DB ALREADY CREATED

################################################

# CONNECT TO MYSQL WORKBENCH
cnx = mysql.connector.connect(user='root', password='tiger',
                              host='localhost')

# CREATE CURSOR
cursor = cnx.cursor()

# INSTANCE DATABASE
DB_NAME = 'dogs_scraping'

################################################

# CREATE TABLES
TABLES = {}
TABLES['breeds'] = (
    " CREATE TABLE IF NOT EXISTS `dogs`.`breeds` ( "
    " `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"
    " `id_breed_group` INT(10) UNSIGNED NOT NULL,"
    " `name` VARCHAR(100) NOT NULL,"
    " `description` TEXT NOT NULL,"
    " `url_image` VARCHAR(256) NOT NULL,"
    " `adaptability_id` INT(10) UNSIGNED NOT NULL,"
    " `height` VARCHAR(100) NULL DEFAULT NULL,"
    " `weight` VARCHAR(100) NULL DEFAULT NULL,"
    " `life_span` VARCHAR(100) NULL DEFAULT NULL,"
    " PRIMARY KEY (`id`),"
    " UNIQUE INDEX `name` (`name` ASC),"
    " INDEX `fk_breed_in_group_idx` (`id_breed_group` ASC),"
    " INDEX `fk_breeds_adaptability1_idx` (`adaptability_id` ASC),"
    " CONSTRAINT `fk_breed_in_group` FOREIGN KEY (`id_breed_group`)"
    "   REFERENCES `dogs`.`breeds_group` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, "
    " CONSTRAINT `fk_breeds_adaptability1` FOREIGN KEY (`adaptability_id`)"
    "   REFERENCES `dogs`.`adaptability` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION"
    ")ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ")

TABLES['breeds_group'] = (
    " CREATE TABLE IF NOT EXISTS `dogs`.`breeds_group` ( "
    " `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"
    " `name` VARCHAR(100) NOT NULL,"
    " PRIMARY KEY (`id`),"
    " UNIQUE INDEX `name` (`name` ASC)) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ")

TABLES['adaptability'] = (
    " CREATE TABLE IF NOT EXISTS `dogs`.`adaptability` ("
    " `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"
    " `apartment_living` INT(11) NOT NULL,"
    " `good_for_novice_owner` TEXT NOT NULL,"
    " `sensitivity` INT(11) NOT NULL,"
    " `tolerates_being_alone` INT(11) NOT NULL,"
    " `tolerates_cold_weather` INT(11) NOT NULL,"
    " `tolerates_hot_weather` INT(11) NOT NULL,"
    " PRIMARY KEY (`id`)) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARACTER SET = utf8 ")

################################################

# CREATE FUNCTION TO CREATE THE DATABASE
def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)


# TRY ACTIVATE THE DATABASE
try:
    cursor.execute(f"USE {DB_NAME}")
except mysql.connector.Error as err:
    print(f"Database {DB_NAME} does not exists.")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print(f"Database {DB_NAME} created successfully.")
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

################################################

# TODO
## NEED TO INSERT DATA FROM CSV/EXCEL (IF CSV YOU NEED
## TO RERUN THE CODE, CSV HAS A BLANK ROW BETWEEN TWO DATA ROWS

##################################################

# FOR EACH TABLE IN TABLES CREATE TABLE AND HANDLING EXCEPTION
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print(f"Creating table {table_name}: ", end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

################################################

# CLOSE CURSOR
cursor.close()

# CLOSE CONNECTION
cnx.close()


# -*- coding: utf-8 -*-
import pandas as pd
import mysql.connector


def insert_row_in_breeds_group(cursor, row):
    query = """INSERT INTO `breeds_group` (`name`) VALUES (%s);"""
    cursor.execute(query, (row.loc['dog_breed_group'],))
    return cursor.lastrowid


def insert_row_in_breeds(cursor, row, last_id_breeds_group):
    query = """INSERT INTO `breeds` (id_breed_group, name, description, url_image, height, weight, life_span) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (last_id_breeds_group,
                           row.loc['name'],
                           row.loc['description'],
                           row.loc['image'],
                           row.loc['height'],
                           row.loc['weight'],
                           row.loc['life_span']))
    return cursor.lastrowid


def insert_row_in_adaptability(cursor, row, last_id_breeds):
    query = """INSERT INTO `adaptability`(`breeds_id`,`adapts_well_to_apartment_living`,`good_for_novice_owners`,
    `sensitivity_level`,`tolerates_being_alone`,`tolerates_cold_weather`,`tolerates_hot_weather`,
    `affectionate_with_family`,`kid_friendly`,`dog_friendly`,`friendly_toward_strangers`,`amount_of_shedding`,
    `drooling_potential`,`easy_to_groom`,`general_health`,`potential_for_weight_gain`,`size`,`easy_to_train`,
    `intelligence`,`potential_for_mouthiness`,`prey_drive`,`tendency_to_bark_or_howl`,`wanderlust_potential`,
    `energy_level`,`intensity`,`exercise_needs`,`potential_for_playfulness`) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    cursor.execute(query, (last_id_breeds,
                           row.loc['adapts_well_to_apartment_living'],
                           row.loc['good_for_novice_owners'],
                           row.loc['sensitivity_level'],
                           row.loc['tolerates_being_alone'],
                           row.loc['tolerates_cold_weather'],
                           row.loc['tolerates_hot_weather'],
                           row.loc['affectionate_with_family'],
                           row.loc['kid_friendly'],
                           row.loc['dog_friendly'],
                           row.loc['friendly_toward_strangers'],
                           row.loc['amount_of_shedding'],
                           row.loc['drooling_potential'],
                           row.loc['easy_to_groom'],
                           row.loc['general_health'],
                           row.loc['potential_for_weight_gain'],
                           row.loc['size'],
                           row.loc['easy_to_train'],
                           row.loc['intelligence'],
                           row.loc['potential_for_mouthiness'],
                           row.loc['prey_drive'],
                           row.loc['tendency_to_bark_or_howl'],
                           row.loc['wanderlust_potential'],
                           row.loc['energy_level'],
                           row.loc['intensity'],
                           row.loc['exercise_needs'],
                           row.loc['potential_for_playfulness']))
    return cursor.lastrowid


# -1: NOT INSERTED YET
# Otherwise return the ID of the group (from the database)
def is_group_already_inserted(groups, target):
    for group in groups:
        if target == group[1]:
            return group[0]
    return -1

#####################################################################
# BUSINESS LOGIC

# CONNECT TO MYSQL
cnx = mysql.connector.connect(user='root',
                              password='tiger',
                              host='localhost',
                              autocommit=True)

# CREATE A CURSOR TO INTERACT WITH MYSQL SERVER USING MYSQLCONNECTION OBJECT
# EXPLANATION OF BUFFERED=TRUE:
# https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
cursor = cnx.cursor(buffered=True)

use_db = 'USE dogs'
cursor.execute(use_db)


# READ THE DATAFRAME. MAINTAIN NULL VALUES AS EMPTY STRING
csv_data = pd.read_csv('out.csv',
                       encoding='utf8',
                       na_filter=False)

breeds_group_duplicate_check = []
for index, row in csv_data.iterrows():

    last_id_breeds_group = is_group_already_inserted(breeds_group_duplicate_check, row.loc['dog_breed_group'])

    if last_id_breeds_group == -1:
        last_id_breeds_group = insert_row_in_breeds_group(cursor, row)
        breeds_group_duplicate_check.append((last_id_breeds_group, row.loc['dog_breed_group']))

    last_id_breeds = insert_row_in_breeds(cursor, row, last_id_breeds_group)
    last_id_adaptability = insert_row_in_adaptability(cursor, row, last_id_breeds)

################################################
# CLOSE THE CURSOR
cursor.close()

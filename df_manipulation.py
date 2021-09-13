# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# ---------------------------------------

# CREATE A FUNCTION TO ROUND CORRECTLY
def fun_to_round_up(number_to_round_up):
    # TAKE THE DEC PART
    dec_part = pd.Series(number_to_round_up - np.fix(number_to_round_up))
    # FOR EACH ELEMENT IF DEC PART GREATER/EQUAL THAN 0.5 THEN CEILING
    for dec_el in dec_part:
        if np.greater_equal(dec_el, 0.50):
            return np.ceil(number_to_round_up)
        else:
            # OTHERWISE FLOOR, BECAUSE DEC PART IS LESS THAN 0.5
            return np.floor(number_to_round_up)

# ---------------------------------------

# READ THE DF
df = pd.read_csv("out.csv", sep=",")

# ---------------------------------------
# CREATE LIST TO USE TO CALCULATE MEAN
# ADAPTABILITY
adaptability_columns = ['adapts_well_to_apartment_living',
                         'good_for_novice_owners',
                         'sensitivity_level',
                         'tolerates_being_alone',
                         'tolerates_cold_weather',
                         'tolerates_hot_weather']

# ALL AROUND FRIENDLINESS
all_around_friendliness_columns = ['affectionate_with_family',
                                   'kid_friendly',
                                   'dog_friendly',
                                   'friendly_toward_strangers']

# HEALTH AND GROOMING NEEDS
health_and_grooming_needs_columns = ['amount_of_shedding',
                                     'drooling_potential',
                                     'easy_to_groom',
                                     'general_health',
                                     'potential_for_weight_gain',
                                     'size']

# TRAINABILITY
trainability_columns = ['easy_to_train',
                        'intelligence',
                        'potential_for_mouthiness',
                        'prey_drive',
                        'tendency_to_bark_or_howl',
                        'wanderlust_potential']

# PHYSICAL NEEDS
physical_needs_columns = ['energy_level',
                          'intensity',
                          'exercise_needs',
                          'potential_for_playfulness']

# ---------------------------------------

# CREATE THE NEW COLUMNS AS A MEAN APPLYING FUN_TO_ROUND() FUNCTION AS A LAMBDA FUNCTION
# ADAPTABILITY
df['adaptability'] = (df[adaptability_columns].mean(axis=1)).apply(lambda x: fun_to_round_up(x))

# ALL AROUND FRIENDLINESS
df['all_around_friendliness'] = (df[all_around_friendliness_columns].mean(axis=1)).apply(lambda x: fun_to_round_up(x))

# HEALTH AND GROOMING NEEDS
df['health_and_grooming_needs'] = (df[health_and_grooming_needs_columns].mean(axis=1)).apply(lambda x: fun_to_round_up(x))

# TRAINABILITY
df['trainability'] = (df[trainability_columns].mean(axis=1)).apply(lambda x: fun_to_round_up(x))

# PHYSICAL NEEDS
df['physical_needs'] = (df[physical_needs_columns].mean(axis=1)).apply(lambda x: fun_to_round_up(x))

# ---------------------------------------

# SAVE THE COLUMN TO MOVE
column_to_move_adaptability = df.pop("adaptability")
column_to_move_friendliness = df.pop("all_around_friendliness")
column_to_move_grooming_needs = df.pop("health_and_grooming_needs")
column_to_move_trainability = df.pop("trainability")
column_to_move_physical_needs = df.pop("physical_needs")

# ---------------------------------------

# INSERT COLUMN WITH INSERT(LOCATION, COLUMN_NME, COLUMN_VALUE)
df.insert(3, "adaptability", column_to_move_adaptability)
df.insert(10, "all_around_friendliness", column_to_move_friendliness)
df.insert(15, "health_and_grooming_needs", column_to_move_grooming_needs)
df.insert(22, "trainability", column_to_move_trainability)
df.insert(29, "physical_needs", column_to_move_physical_needs)

# ---------------------------------------

# EXPORT TO CSV
df.to_csv('new_out.csv', index=False)

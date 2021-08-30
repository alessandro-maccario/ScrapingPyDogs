# -*- coding: utf-8 -*-
import csv
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


# CLASS DOG
class Dog:

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

    # SET BASIC FIELDS
    def set_description(self, description):
        self.description = description

    def set_image(self, image):
        self.image = image

    # SET ADAPTABILITY FIELDS
    def set_adapts_well_to_apartment_living(self, adapts_well_to_apartment_living):
        self.adapts_well_to_apartment_living = adapts_well_to_apartment_living

    def set_good_for_novice_owners(self, good_for_novice_owners):
        self.good_for_novice_owners = good_for_novice_owners

    def set_sensitivity_level(self, sensitivity_level):
        self.sensitivity_level = sensitivity_level

    def set_tolerates_being_alone(self, tolerates_being_alone):
        self.tolerates_being_alone = tolerates_being_alone

    def set_tolerates_cold_weather(self, tolerates_cold_weather):
        self.tolerates_cold_weather = tolerates_cold_weather

    def set_tolerates_hot_weather(self, tolerates_hot_weather):
        self.tolerates_hot_weather = tolerates_hot_weather

    # SET ALL AROUND FRIENDLINESS FIELDS
    def set_affectionate_with_family(self, affectionate_with_family):
        self.affectionate_with_family = affectionate_with_family

    def set_kid_friendly(self, kid_friendly):
        self.kid_friendly = kid_friendly

    def set_dog_friendly(self, dog_friendly):
        self.dog_friendly = dog_friendly

    def set_friendly_toward_strangers(self, friendly_toward_strangers):
        self.friendly_toward_strangers = friendly_toward_strangers

    # SET HEALTH AND GROOMING NEEDS FIELDS
    def set_amount_of_shedding(self, amount_of_shedding):
        self.amount_of_shedding = amount_of_shedding

    def set_drooling_potential(self, drooling_potential):
        self.drooling_potential = drooling_potential

    def set_easy_to_groom(self, easy_to_groom):
        self.easy_to_groom = easy_to_groom

    def set_general_health(self, general_health):
        self.general_health = general_health

    def set_potential_for_weight_gain(self, potential_for_weight_gain):
        self.potential_for_weight_gain = potential_for_weight_gain

    def set_size(self, size):
        self.size = size

    # SET TRAINABILITY FIELDS
    def set_easy_to_train(self, easy_to_train):
        self.easy_to_train = easy_to_train

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def set_potential_for_mouthiness(self, potential_for_mouthiness):
        self.potential_for_mouthiness = potential_for_mouthiness

    def set_prey_drive(self, prey_drive):
        self.prey_drive = prey_drive

    def set_tendency_to_bark_or_howl(self, tendency_to_bark_or_howl):
        self.tendency_to_bark_or_howl = tendency_to_bark_or_howl

    def set_wanderlust_potential(self, wanderlust_potential):
        self.wanderlust_potential = wanderlust_potential

    # SET PHYSICAL NEEDS FIELDS
    def set_energy_level(self, energy_level):
        self.energy_level = energy_level

    def set_intensity(self, intensity):
        self.intensity = intensity

    def set_exercise_needs(self, exercise_needs):
        self.exercise_needs = exercise_needs

    def set_potential_for_playfulness(self, potential_for_playfulness):
        self.potential_for_playfulness = potential_for_playfulness

    # SET VITAL STATS FIELDS
    def set_dog_breed_group(self, dog_breed_group):
        self.dog_breed_group = dog_breed_group

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_life_span(self, life_span):
        self.life_span = life_span


# CONNECT TO THE WEB SITE AND USE USER-AGENT TO FAKE THE CONNECTION BY A HUMAN #####
def get_beautiful_soup(url):
    # Open the URL as Browser, not as python urllib
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    # data = infile.decode('utf-8')
    data = infile.decode('ascii','ignore')
    return BeautifulSoup(data, 'html.parser', exclude_encodings=["ISO-8859-7"])

# FUNCTION TO GET DOG'S NAME
def get_dogs_name(soup):
    names = []
    for name in soup.find_all("a", class_="list-item-title"):
        names.append(name.text)

    # CONVERT TO LOWER CASE, REQUIRED TO ADD THE DOG'S NAME TO THE URL
    return [x.lower() for x in names]


# BUSINESS LOGIC
soup = get_beautiful_soup("https://dogtime.com/dog-breeds/profiles")
names = get_dogs_name(soup)

print(names)
print("Lunghezza lista: ", len(names))
# exit()

# ALL DOGS
dogs = []
not_find = []

# TEST ONLY FOR FIRST 5 ROWS
test_5_rows = 0
for index, name in enumerate(names):
    if test_5_rows == 3:
        break
    else:
        test_5_rows += 1
        try:
            # GET EACH PAGE WITH A DIFFERENT DOG'S NAME
            soup = get_beautiful_soup(f"https://dogtime.com/dog-breeds/{name.replace(' ', '-')}")
        except:
            not_find.append(name)
            continue

        # FIND THE RIGHT CLASS WHERE TO FIND INTRO, IMAGE
        intro = soup.find("div", {"class": "breeds-single-intro"})
        image = intro.find('img')['data-lazy-src']

        # GET DESCRIPTION FROM THE TOP OF THE PAGE
        description_elements = intro.find_all('p')[:-2]
        final_description = ''
        for sentence in description_elements:
            final_description += sentence.text

        # GET THE STARS FROM THE DOG'S CHARACTERISTICS OF THE PAGE
        stars = soup.find_all("div", {"class": "characteristic-star-block"})
        stars_list = []
        for star in stars:
            stars_list.append(star.text)
            stars_list = [x for x in stars_list if x]

        # print("Stars list: ", stars_list)
        # GET VITAL STATS LIST
        vital_stats = soup.find_all("div", {"class": "vital-stat-box"})

        vital_stats_list = []
        for vital_field in vital_stats:
            vital_stats_list.append(vital_field.text)
            vital_stats_list = [x for x in vital_stats_list if x]

        vital_stats_final = []
        for element in vital_stats_list:
            # FIND THE INDEX OF ":"
            i = element.index(":")
            # USE THAT INDEX TO FIND THE SUBSTRING TO STRIP
            element = element[i + 1:].strip()
            vital_stats_final.append(element)


        # DOG OBJECT
        dog = Dog(name)
        dog.set_description(final_description)
        dog.set_image(image)
        print(index, dog.name)

        # TODO
        ## AGGIUNGERE CAMPO ADAPTABILITY CHE SIA SOMMA, ROUND E DIVISIONE PER I VALORI DA 0
        ## A 5 PRESENTI DEI SINGOLI ELEMENTI

        try:
            # ADAPTABILITY
            dog.set_adapts_well_to_apartment_living(stars_list[0])
            dog.set_good_for_novice_owners(stars_list[1])
            dog.set_sensitivity_level(stars_list[2])
            dog.set_tolerates_being_alone(stars_list[3])
            dog.set_tolerates_cold_weather(stars_list[4])
            dog.set_tolerates_hot_weather(stars_list[5])

            # ALL ROUND FRIENDLINESS
            dog.set_affectionate_with_family(stars_list[6])
            dog.set_kid_friendly(stars_list[7])
            dog.set_dog_friendly(stars_list[8])
            dog.set_friendly_toward_strangers(stars_list[9])

            # HEALTH AND GROOMING NEEDS
            dog.set_amount_of_shedding(stars_list[10])
            dog.set_drooling_potential(stars_list[11])
            dog.set_easy_to_groom(stars_list[12])
            dog.set_general_health(stars_list[13])
            dog.set_potential_for_weight_gain(stars_list[14])
            dog.set_size(stars_list[15])

            # TRAINABILITY
            dog.set_easy_to_train(stars_list[16])
            dog.set_intelligence(stars_list[17])
            dog.set_potential_for_mouthiness(stars_list[18])
            dog.set_prey_drive(stars_list[19])
            dog.set_tendency_to_bark_or_howl(stars_list[20])
            dog.set_wanderlust_potential(stars_list[21])

            # PHYSICAL NEEDS
            dog.set_energy_level(stars_list[22])
            dog.set_intensity(stars_list[23])
            dog.set_exercise_needs(stars_list[24])
            dog.set_potential_for_playfulness(stars_list[25])

            # VITAL STATS
            dog.set_dog_breed_group(vital_stats_final[0])
            dog.set_height(vital_stats_final[1])
            dog.set_weight(vital_stats_final[2])
            dog.set_life_span(vital_stats_final[3])
        except:
            continue

        print("----------------")

        # TEST PRINT
        # print(index, dog.name)
        # print(dog.image)
        # print(dog.description)
        # print(dog.adapts_well_to_apartment_living)
        # print(dog.good_for_novice_owners)
        # print(dog.sensitivity_level)
        # print(dog.tolerates_being_alone)
        # print(dog.tolerates_cold_weather)
        # print(dog.tolerates_hot_weather)

        # APPEND TO FINAL LIST: EACH ELEMENT IN THIS LIST WILL BE OUR ROW FOR EACH DOG
        dogs.append(dog)

#####################################################################
#
# with open('out.csv','w',newline='') as f:
#     # fieldnames lists the headers for the csv.
#     w = csv.DictWriter(f,fieldnames=sorted(dir(dogs[0])))
#     w.writeheader()
#
#     for obj in dogs:
#         # Build a dictionary of the member names and values...
#         w.writerow({k:getattr(obj,k) for k in dir(dogs)})


#
# print(Dog.get_list())
#####################################################################

print("Dogs not found: ", not_find)

# CONVERTING TO EXCEL AND CSV
pd.DataFrame(dogs).to_excel('dogs_output.xlsx', header=False)
pd.DataFrame(dogs).to_csv('dogs_output.csv', header=False)

# TODO:
## MYSQL INSERT OR CREATE A NEW SQL DATABASE FROM SCRATCH WITH PYTHON

# -*- coding: utf-8 -*-
import csv
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

#####################################################################
# CREATE CLASS DOG
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

#####################################################################

# CONNECT TO THE WEB SITE AND USE USER-AGENT TO FAKE THE CONNECTION BY A HUMAN #####
def get_beautiful_soup(url):
    # Open the URL as Browser, not as python urllib
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    # data = infile.decode('utf-8')
    data = infile.decode('ascii','ignore')
    return BeautifulSoup(data, 'lxml', exclude_encodings=["ISO-8859-7"])

# FUNCTION TO GET DOG'S NAME
def get_dogs_name(soup):
    names = []
    for name in soup.find_all("a", class_="list-item-title"):
        names.append(name.text)

    # CONVERT TO LOWER CASE, REQUIRED TO ADD THE DOG'S NAME TO THE URL
    return [x.lower() for x in names]

#####################################################################
# BUSINESS LOGIC
soup = get_beautiful_soup("https://dogtime.com/dog-breeds/profiles")
names = get_dogs_name(soup)

print(names)
print("LENGTH OF THE DOGS LIST: ", len(names))

# LIST OF ALL DOGS
dogs = []
# IF DOGS NOT FOUND (BECAUSE DIFFERENT LINK) INSERT IN THIS LIST
not_find = []

#####################################################################
# DOWNLOADING DATA

for index, name in enumerate(names):
    # DEALING WITH DIFFERENT URL DOGS NAME
    if name == "korean jindo dog":
        soup = get_beautiful_soup("https://dogtime.com/dog-breeds/jindo")
    elif name == "mutt (mixed)":
        soup = get_beautiful_soup("https://dogtime.com/dog-breeds/mutt")
    elif name == "petit basset griffon venden":
        soup = get_beautiful_soup("https://dogtime.com/dog-breeds/petit-basset-griffon-vendeen")
    elif name == "xoloitzcuintli":
        soup = get_beautiful_soup("https://dogtime.com/dog-breeds/xoloitzuintli")
    elif name == "australian shepherd husky":
        soup = get_beautiful_soup("https://dogtime.com/dog-breeds/australian-shepherd-husky")
    else:
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
    description_elements = intro.find_all('p')[:-1]
    final_description = ''
    for sentence in description_elements:
        final_description += sentence.text

    # GET THE STARS FROM THE DOG'S CHARACTERISTICS OF THE PAGE
    stars = soup.find_all("div", {"class": "characteristic-star-block"})
    stars_list = []
    for star in stars:
        stars_list.append(star.text)
        stars_list = [x for x in stars_list if x]

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

    # CREATE DOG OBJECT
    dog = Dog(name)
    print(index, dog.name)

    # TAKE IMPORTANT ELEMENTS OF THE PAGE
    # INITIAL DESCRIPTION
    dog.set_description(final_description)
    # IMAGE
    dog.set_image(image)

    # GET ALL THE DOGS CHARACTERISTICS
    # 1. ADAPTABILITY
    try:
        dog.set_adapts_well_to_apartment_living(stars_list[0])
    except:
        dog.set_adapts_well_to_apartment_living("")
    try:
        dog.set_good_for_novice_owners(stars_list[1])
    except:
        dog.set_good_for_novice_owners("")
    try:
        dog.set_sensitivity_level(stars_list[2])
    except:
        dog.set_sensitivity_level("")
    try:
        dog.set_tolerates_being_alone(stars_list[3])
    except:
        dog.set_tolerates_being_alone("")
    try:
        dog.set_tolerates_cold_weather(stars_list[4])
    except:
        dog.set_tolerates_cold_weather("")
    try:
        dog.set_tolerates_hot_weather(stars_list[5])
    except:
        dog.set_tolerates_hot_weather("")

    # 2. ALL ROUND FRIENDLINESS
    try:
        dog.set_affectionate_with_family(stars_list[6])
    except:
        dog.set_affectionate_with_family("")
    try:
        dog.set_kid_friendly(stars_list[7])
    except:
        dog.set_kid_friendly("")
    try:
        dog.set_dog_friendly(stars_list[8])
    except:
        dog.set_dog_friendly("")
    try:
        dog.set_friendly_toward_strangers(stars_list[9])
    except:
        dog.set_friendly_toward_strangers("")

    # 3. HEALTH AND GROOMING NEEDS
    try:
        dog.set_amount_of_shedding(stars_list[10])
    except:
        dog.set_amount_of_shedding("")
    try:
        dog.set_drooling_potential(stars_list[11])
    except:
        dog.set_drooling_potential("")
    try:
        dog.set_easy_to_groom(stars_list[12])
    except:
        dog.set_easy_to_groom("")
    try:
        dog.set_general_health(stars_list[13])
    except:
        dog.set_general_health("")
    try:
        dog.set_potential_for_weight_gain(stars_list[14])
    except:
        dog.set_potential_for_weight_gain("")
    try:
        dog.set_size(stars_list[15])
    except:
        dog.set_size("")

    # 4. TRAINABILITY
    try:
        dog.set_easy_to_train(stars_list[16])
    except:
        dog.set_easy_to_train("")
    try:
        dog.set_intelligence(stars_list[17])
    except:
        dog.set_intelligence("")
    try:
        dog.set_potential_for_mouthiness(stars_list[18])
    except:
        dog.set_potential_for_mouthiness("")
    try:
        dog.set_prey_drive(stars_list[19])
    except:
        dog.set_prey_drive("")
    try:
        dog.set_tendency_to_bark_or_howl(stars_list[20])
    except:
        dog.set_tendency_to_bark_or_howl("")
    try:
        dog.set_wanderlust_potential(stars_list[21])
    except:
        dog.set_wanderlust_potential("")

    # 5. PHYSICAL NEEDS
    try:
        dog.set_energy_level(stars_list[22])
    except:
        dog.set_energy_level("")
    try:
        dog.set_intensity(stars_list[23])
    except:
        dog.set_intensity("")
    try:
        dog.set_exercise_needs(stars_list[24])
    except:
        dog.set_exercise_needs("")
    try:
        dog.set_potential_for_playfulness(stars_list[25])
    except:
        dog.set_potential_for_playfulness("")

    # VITAL STATS
    try:
        dog.set_dog_breed_group(vital_stats_final[0])
    except:
        dog.set_dog_breed_group("")
    try:
        dog.set_height(vital_stats_final[1])
    except:
        dog.set_height("")
    try:
        dog.set_weight(vital_stats_final[2])
    except:
        dog.set_weight("")
    try:
        dog.set_life_span(vital_stats_final[3])
    except:
        dog.set_life_span("")

    # APPEND TO FINAL LIST: EACH ELEMENT IN THIS LIST WILL BE OUR ROW FOR EACH DOG
    print("--------- PRINTING INSIDE DATASET ---------")
    dogs.append(dog)
    print("--------- NEXT ---------")

#####################################################################
# # WRITING RESULTS TO CSV
with open('out.csv','w') as f:
    # fieldnames lists the headers for the csv.
    w = csv.DictWriter(f,fieldnames=vars(dogs[0]))
    w.writeheader()

    for obj in dogs:
        # Build a dictionary of the member names and values...
        w.writerow({k:getattr(obj,k) for k in vars(obj)})


# CONVERT TO XLSX
df = pd.read_csv("out.csv")
df.to_excel("out.xlsx", index=False)
#####################################################################


#####################################################################
# TODO:
## TREAT SINGLE PAGES OF THE DOGS NOT FOUND SEPARATELY
print("Dogs not found: ", not_find)
#####################################################################


#####################################################################
# TODO:
## MYSQL INSERT OR CREATE A NEW SQL DATABASE FROM SCRATCH WITH PYTHON
#####################################################################
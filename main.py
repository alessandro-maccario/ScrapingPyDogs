# -*- coding: utf-8 -*-
from dog_object import *



#####################################################################
# BUSINESS LOGIC

# For development purpose
dev = True
max_rows = 15

# LIST OF ALL DOGS
dogs = []

soup = get_beautiful_soup("https://dogtime.com/dog-breeds/profiles")
names = get_dogs_name(soup)

print(names)
print("LENGTH OF THE DOGS LIST: ", len(names))

#####################################################################
# DOWNLOADING DATA

for index, name in enumerate(names):

    # Only for development purpose
    if dev:
        if index == max_rows:
            print("===>>> WARNING: THIS IS ONLY DEVELOPMENT!")
            break

    # Get dog name (soup)
    soup = get_soup_dog(name)

    # FIND THE RIGHT CLASS WHERE TO FIND INTRO, IMAGE
    intro = soup.find("div", {"class": "breeds-single-intro"})
    image = intro.find('img')['data-lazy-src']

    # GET DESCRIPTION FROM THE TOP OF THE PAGE
    description = get_description_from_top_page(intro)

    # GET THE STARS FROM THE DOG'S CHARACTERISTICS OF THE PAGE
    stars = soup.find_all("div", {"class": "characteristic-star-block"})
    stars_list = get_text_from_stars(stars)

    # GET VITAL STATS LIST
    vital_stats = soup.find_all("div", {"class": "vital-stat-box"})

    group = get_group(vital_stats)
    height = get_height(vital_stats)
    weight = get_weight(vital_stats)
    life_span = get_life_span(vital_stats)

    # CREATE DOG OBJECT
    dog = Dog(name)
    dog.set_image(image)
    dog.set_description(description)

    # GET ALL THE DOGS CHARACTERISTICS
    try:
        # 1. ADAPTABILITY
        dog.set_adapts_well_to_apartment_living(stars_list[0])
        dog.set_good_for_novice_owners(stars_list[1])
        dog.set_sensitivity_level(stars_list[2])
        dog.set_tolerates_being_alone(stars_list[3])
        dog.set_tolerates_cold_weather(stars_list[4])
        dog.set_tolerates_hot_weather(stars_list[5])
        # 2. ALL ROUND FRIENDLINESS
        dog.set_affectionate_with_family(stars_list[6])
        dog.set_kid_friendly(stars_list[7])
        dog.set_dog_friendly(stars_list[8])
        dog.set_friendly_toward_strangers(stars_list[9])
        # 3. HEALTH AND GROOMING NEEDS
        dog.set_amount_of_shedding(stars_list[10])
        dog.set_drooling_potential(stars_list[11])
        dog.set_easy_to_groom(stars_list[12])
        dog.set_general_health(stars_list[13])
        dog.set_potential_for_weight_gain(stars_list[14])
        dog.set_size(stars_list[15])
        # 4. TRAINABILITY
        dog.set_easy_to_train(stars_list[16])
        dog.set_intelligence(stars_list[17])
        dog.set_potential_for_mouthiness(stars_list[18])
        dog.set_prey_drive(stars_list[19])
        dog.set_tendency_to_bark_or_howl(stars_list[20])
        dog.set_wanderlust_potential(stars_list[21])
        # 5. PHYSICAL NEEDS
        dog.set_energy_level(stars_list[22])
        dog.set_intensity(stars_list[23])
        dog.set_exercise_needs(stars_list[24])
        dog.set_potential_for_playfulness(stars_list[25])
    except:
        print("Error in set dog characteristics!")

    dog.set_dog_breed_group(group)
    dog.set_height(height)
    dog.set_weight(weight)
    dog.set_life_span(life_span)

    print(dog.__dict__)

    # APPEND TO FINAL LIST: EACH ELEMENT IN THIS LIST WILL BE OUR ROW FOR EACH DOG
    dogs.append(dog)

#####################################################################
write_to_csv(dogs)
convert_csv_to_excel()
#####################################################################

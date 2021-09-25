# -*- coding: utf-8 -*-
from dog import Dog
from lib import *

#####################################################################
# BUSINESS LOGIC

# For development purpose
dev = False
max_rows = 20

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
    info_stars = soup.find_all("a", {"class": "characteristic-stars"})

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
    dog.set_dog_breed_group(group)
    dog.set_height(height)
    dog.set_weight(weight)
    dog.set_life_span(life_span)

    # Set characteristics (dynamically)
    for info_star in info_stars:

        # Get title and value of the characteristic
        characteristic_title = info_star.find("div", {"class": "characteristic-title"}).get_text()
        characteristic_star = info_star.find("div", {"class": "star"}).get_text()

        # Create a method name dynamically, based on the title of the characteristic (e.g. set_kid_friendly)
        # Concatenate 'set_' and the lower title (and replace whitespaces and dashes)
        method_name = 'set_' + characteristic_title.lower().replace(" ", "_").replace("-", "_")

        # Return the reference of the method of the dog
        method_to_call = getattr(dog, method_name)

        # Use the method of the dog
        result = method_to_call(characteristic_star)

    print(dog.__dict__)

    # APPEND TO FINAL LIST: EACH ELEMENT IN THIS LIST WILL BE OUR ROW FOR EACH DOG
    dogs.append(dog)

#####################################################################
write_to_csv(dogs)
convert_csv_to_excel()
#####################################################################

# -*- coding: utf-8 -*-
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


# CONNECT TO THE WEB SITE AND USE USER-AGENT TO FAKE THE CONNECTION BY A HUMAN #####
def get_beautiful_soup(url):
    # Open the URL as Browser, not as python urllib
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    data = infile.decode('utf-8')
    return BeautifulSoup(data, 'html.parser')


def get_dogs_name(soup):
    names = []
    for name in soup.find_all("a", class_="list-item-title"):
        names.append(name.text)

    # CONVERT TO LOWER CASE, REQUIRED TO ADD THE DOG'S NAME TO THE URL
    return [x.lower() for x in names]


# BUSINESS LOGIC
soup = get_beautiful_soup("https://dogtime.com/dog-breeds/profiles")
names = get_dogs_name(soup)
# print(names)

# ALL DOGS
dogs = []
for name in names:
    soup = get_beautiful_soup(f"https://dogtime.com/dog-breeds/{name.replace(' ', '-')}")

    # TAKE ONLY THE PARAGRAPHS AT THE TOP OF THE WEBSITE
    intro = soup.find("div", {"class": "breeds-single-intro"})
    image = intro.find('img')['data-lazy-src']

    description_elements = intro.find_all('p')[:-2]
    final_description = ''
    for sentence in description_elements:
        final_description += sentence.text

    # Dog object
    dog = Dog(name)
    dog.set_description(final_description)
    dog.set_image(image)
    # dog.set_adapts_well_to_apartment_living(3)
    # dog.set_good_for_novice_owners(2)
    # dog.set_sensitivity_level(3)

    print(dog.image)
    print(dog.description)
    # print(dog.adapts_well_to_apartment_living)
    # print(dog.good_for_novice_owners)
    # print(dog.sensitivity_level)

    dogs.append(dog)

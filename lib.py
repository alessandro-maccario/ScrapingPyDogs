import csv
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

#####################################################################
# CONNECT TO THE WEB SITE AND USE USER-AGENT TO SIMULATE THE CONNECTION BY A HUMAN #####


def get_beautiful_soup(url):
    # Open the URL as Browser, not as python urllib
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    infile = urllib.request.urlopen(page).read()
    # data = infile.decode('utf-8')
    data = infile.decode('ascii', 'ignore')
    return BeautifulSoup(data, 'lxml', exclude_encodings=["ISO-8859-7"])


def get_dogs_name(soup):
    names = []
    for name in soup.find_all("a", class_="list-item-title"):
        names.append(name.text)

    # CONVERT TO LOWER CASE, REQUIRED TO ADD THE DOG'S NAME TO THE URL
    return [x.lower() for x in names]


def get_description_from_top_page(intro):
    description_elements = intro.find_all('p')[:-1]
    final_description = ''
    for sentence in description_elements:
        final_description += sentence.text
    return final_description


# DEALING WITH DIFFERENT URL DOGS NAME
def get_soup_dog(name):
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
        # GET EACH PAGE WITH A DIFFERENT DOG'S NAME
        soup = get_beautiful_soup(f"https://dogtime.com/dog-breeds/{name.replace(' ', '-')}")
    return soup


def get_group(vital_stats):
    return vital_stats[0].get_text().split(':')[1]


def get_height(vital_stats):
    for element in vital_stats:
        if 'inches' in element.get_text():
            return element.get_text().split(':')[1]
    return ""


def get_weight(vital_stats):
    for element in vital_stats:
        if 'pounds' in element.get_text():
            return element.get_text().split(':')[1]
    return ""


def get_life_span(vital_stats):
    for element in vital_stats:
        if 'years' in element.get_text():
            return element.get_text().split(':')[1]
    return ""


def write_to_csv(dogs):
    with open('out.csv', 'w', newline='') as f:

        for index, dog in enumerate(dogs):
            if index == 0:
                # fieldnames lists the headers for the csv.
                w = csv.DictWriter(f, fieldnames=vars(dogs[0]))
                w.writeheader()

            # Build a dictionary of the member names and values...
            w.writerow({k: getattr(dog, k) for k in vars(dog)})


def convert_csv_to_excel():
    df = pd.read_csv("out.csv")
    df.to_excel("out.xlsx", index=False)
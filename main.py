import urllib.request
from bs4 import BeautifulSoup

##### CONNECT TO THE WEB SITE AND USE USER-AGENT TO FAKE THE CONNECTION BY A HUMAN #####
url_names = "https://dogtime.com/dog-breeds/profiles"
# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url_names, headers = {'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1



##### USE OF BEAUTIFUL SOUP #####
# print(data) # Print the data to the screen

soup = BeautifulSoup(data, 'html.parser')

##### CREATE A PANDAS SERIES TO TAKE CARE OF ALL THE DOGS NAME #####
# TODO
# 1. Crea una lista che contenga tutti i nomi dei cani
# 2. Converti la lista in Serie
# 3. Concatena più liste con tutti i dati dei cani
# 4. Convertilo in DataFrame

## CREATE LISTS VARIABLE TO STORE INFORMATION

# NAMES' LIST
name_l = []

# DESCRIPTION'S LIST
desc_l = []

# URL'S IMAGE LIST
url_image_l = []

# DOG'S HEIGHT LIST
height_l = []

# DOG'S WEIGHT LIST
weight_l = []

# DOG'S LIFE SPAN LIST
life_span_l = []

# CREATE DOG'S LIST NAMES
for name in soup.find_all("a", class_="list-item-title"):
    name_l.append(name.text)


#### TEST ####

## crea un branch per vedere se risci, per un singolo nome a collegarti alla pagina e a tirare giù le info
## se funziona fanne un ?rebase?? (o merge) e vai avanti


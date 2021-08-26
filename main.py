# -*- coding: utf-8 -*-
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
## 1. Crea una lista che contenga tutti i nomi dei cani
## 2. Converti la lista in Serie
## 3. Concatena più liste con tutti i dati dei cani
## 4. Convertilo in DataFrame

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

## CONVERT TO LOWER CASE, REQUIRED TO ADD THE DOG'S NAME TO THE URL
name_l = [x.lower() for x in name_l]

#### NUOVO BRANCH "test_data_single_page ####
# TODO
## Nel nuovo branch collegarsi alla pagina di un singolo cane e tirare giù le info necessarie in base alle liste
## create precedentemente
## Se funziona fanne un ?rebase?? (o merge) e vai avanti facendo la stessa cosa ma per tutti i nomi nella lista
## dei nomi dei cani.
## CONVERTIRE IL SEGUENTE CODICE IN UNA FUNZIONE CHE FACCIA LA STESSA COSA: ARGOMENTI --> NOME DEL CANE, URL
## CHE DEVE ESSERE INTEGRATO COL NOME DEL CANE

## FIRST DOG: AFADOR
url_afador = "https://dogtime.com/dog-breeds/afador"
# Open the URL as Browser, not as python urllib
page_afador = urllib.request.Request(url_afador, headers={'User-Agent': 'Mozilla/5.0'})
infile_afador = urllib.request.urlopen(page_afador).read()
# Read the content as string decoded with ISO-8859-1
data_afador = infile_afador.decode('utf-8')

##### USE OF BEAUTIFUL SOUP #####
soup_afador = BeautifulSoup(data_afador, 'html.parser')

# TAKE ONLY THE PARAGRAPHS AT THE TOP OF THE WEBSITE
description_afador = soup_afador.find_all("p")[0:3]

# APPEND TO THE CORRECT LIST
for sentence in test_1:
    desc_l.append(sentence.text)

# JOIN THE DIFFERENT STRINGS IN LIST AND CONVERT TO A LIST AGAIN
desc_l = [' '.join(string for string in desc_l)]

print(desc_l)


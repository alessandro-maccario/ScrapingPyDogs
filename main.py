import urllib.request
from bs4 import BeautifulSoup

##### CONNECT TO THE WEB SITE #####
url = "https://dogtime.com/dog-breeds/profiles"
# Open the URL as Browser, not as python urllib
page = urllib.request.Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
infile = urllib.request.urlopen(page).read()
data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1

##### USE OF BEAUTIFUL SOUP #####
# print(data) # Print the data to the screen

soup = BeautifulSoup(data, 'html.parser')

##### CREATE A PANDAS SERIES TO TAKE CARE OF ALL THE DOGS NAME #####
# TO DO
# 1. Crea un dataframe vuoto
# 2. Crea la serie con i nomi dei cani
# 3. Aggiungi la serie al dataframe

for name in soup.find_all("a", class_="list-item-title"):
    print(name.text)




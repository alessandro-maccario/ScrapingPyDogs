![james-barker-v3-zcCWMjgM-unsplash](https://user-images.githubusercontent.com/61615072/130869144-886b678e-69f1-4a89-aea1-c777d9003a76.jpg)
Photo by James Barker on Unsplash

# ScrapingPyDogs
Scraping dogs information from *https://dogtime.com/* to save the data into a MySQL database. 
This is an experiment to improve my knowledge of Python and MySQL.

There are three main files:
- *main.py*
  - Scraping all the information of the dogs and export them to a csv and excel files;
- *dogs.sql*
  - Database creation file;
- *insert_into_db.py*
  - Get the csv file and save the information into MySQL database;
- *df_manipulation.py*
  - WIP --> The idea of this file is to calculate the mean of some dogs attributes;

## Example query
Get all the Mastiff of Working Dogs types ordered by *adapts_well_to_apartment_living*:
```
SELECT breeds.name, breeds_group.name, breeds.life_span, adaptability.adapts_well_to_apartment_living
FROM dogs.breeds
JOIN breeds_group ON breeds_group.id = breeds.id_breed_group
JOIN adaptability ON adaptability.breeds_id = breeds.id
WHERE breeds_group.name = 'Working Dogs' AND breeds.name LIKE '%mastiff'
ORDER BY adaptability.adapts_well_to_apartment_living DESC, breeds.name ASC;
```